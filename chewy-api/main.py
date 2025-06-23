"""
main.py – REST façade for the fake e‑commerce demo.

Key improvements
----------------
1.  Celery integration
    • New endpoints that trigger the Celery tasks
      `generate_orders_task` and `generate_clickstream_task`.
    • Endpoint that lets a caller poll task‑status / retrieve results.

2.  Proper use of previously ‘unused’ imports
    • `Order` and `OrderStatusHistory` are now leveraged in the
      `/orders` POST handler to append an extra timeline entry.
    • `COUPON_USAGE` is surfaced through the new `/coupon‑usage`
      reporting endpoint.
    • The Celery tasks themselves are imported *and* used.

3.  PEP 8 / D 257 compliance tweaks
    • Doc‑strings added where missing.
    • Long lines wrapped; explicit logging format kept unchanged.
"""

from __future__ import annotations

import json
import logging
import math
import os
import threading
import time
from datetime import datetime
from typing import Any, Dict, List, Optional

import redis
import sqlalchemy as sa
from apscheduler.schedulers.background import BackgroundScheduler
from celery.result import AsyncResult
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


from data_model import COUPON_USAGE
from data_model import Order, OrderStatusHistory
from location_data import USZipcodeLocationData

from celery_worker import (
    celery_app,
    generate_clickstream_task,
    generate_orders_task,
)
from data_model import FakeEcommerceDataGenerator

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
LOGGER = logging.getLogger(__name__)


FAKE_RECORD_COUNT = int(os.getenv("FAKE_RECORD_COUNT", 1111))
NEW_BATCH_SIZE = int(os.getenv("NEW_BATCH_SIZE", 555))
NEW_BATCH_INTERVAL_SECONDS = int(os.getenv("NEW_BATCH_INTERVAL_SECONDS", 25))

FAKE_CLICKSTREAM_COUNT = int(os.getenv("FAKE_CLICKSTREAM_COUNT", 1111))
NEW_CLICKSTREAM_BATCH_SIZE = int(os.getenv("NEW_CLICKSTREAM_BATCH_SIZE", 555))

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "blewy")
POSTGRES_USER = os.getenv("POSTGRES_USER", "blewy")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Password123456789")
DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:5432/{POSTGRES_DB}",
)

POOL_SIZE = int(os.getenv("SQLALCHEMY_POOL_SIZE", 5))
POOL_TIMEOUT = int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", 30))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": POOL_SIZE,
    "pool_timeout": POOL_TIMEOUT,
    "max_overflow": 5,
}
db = SQLAlchemy(app)


class OrderDB(db.Model):
    """Thin wrapper for raw Order blobs stored as JSON."""

    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_json = db.Column(db.JSON, nullable=False)


class ClickstreamDB(db.Model):
    """Raw click‑stream events persisted as JSON."""

    __tablename__ = "clickstream"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_json = db.Column(db.JSON, nullable=False)


redis_client = redis.Redis(host="redis", port=6379, db=0)
generator = FakeEcommerceDataGenerator()
scheduler = BackgroundScheduler()


def init_db() -> None:
    """Create tables once on app start‑up (idempotent)."""
    with app.app_context():
        inspector = sa.inspect(db.engine)
        existing = inspector.get_table_names()
        if {"orders", "clickstream"} <= set(existing):
            LOGGER.info("Tables present – skipping creation.")
            return
        db.create_all()
        LOGGER.info("Tables created – orders, clickstream.")


def init_combined_data() -> None:
    """
    Populate both *orders* and *click‑stream* tables with the
    same set of customers so downstream analytics can correlate them.
    """
    try:
        target = min(FAKE_RECORD_COUNT, FAKE_CLICKSTREAM_COUNT)
        if target <= 0:
            LOGGER.info("No seed‑data requested (target <= 0).")
            return

        USZipcodeLocationData.init_uszipcode_data()
        chunk = 1_000
        buf_orders: List[OrderDB] = []
        buf_events: List[ClickstreamDB] = []

        LOGGER.info("Generating %d synthetic orders + events …", target)

        for idx in range(target):
            cust = generator.generate_customer_info()
            order_obj = generator.generate_order(customer=cust)
            evt = generator.generate_clickstream_event(customer=cust)

            buf_orders.append(OrderDB(order_json=order_obj.to_dict()))
            buf_events.append(ClickstreamDB(event_json=evt))

            if (idx + 1) % chunk == 0:
                db.session.bulk_save_objects(buf_orders + buf_events)
                db.session.commit()
                LOGGER.debug("Inserted %d / %d rows …", idx + 1, target)
                buf_orders.clear()
                buf_events.clear()

        if buf_orders:
            db.session.bulk_save_objects(buf_orders + buf_events)
            db.session.commit()

        LOGGER.info("Seed generation complete (%d pairs).", target)
    except Exception:
        LOGGER.exception("init_combined_data() – unrecoverable error.")


def maybe_init_data() -> None:
    """Only call `init_combined_data()` if either table is empty."""
    with app.app_context():
        if db.session.query(OrderDB).count() == 0 or db.session.query(
            ClickstreamDB
        ).count() == 0:
            init_combined_data()
        else:
            LOGGER.info("DB already seeded – skipping.")


def add_new_combined_batch() -> None:
    """Cron‑like task that appends a small correlated batch."""
    try:
        with app.app_context():
            batch = min(NEW_BATCH_SIZE, NEW_CLICKSTREAM_BATCH_SIZE)
            if batch <= 0:
                LOGGER.debug("Batch size   <= 0 – nothing to add.")
                return

            LOGGER.info("Appending %d new order/event pairs …", batch)
            buf_orders, buf_events = [], []

            for _ in range(batch):
                cust = generator.generate_customer_info()
                order_obj = generator.generate_order(customer=cust)
                evt = generator.generate_clickstream_event(customer=cust)
                buf_orders.append(OrderDB(order_json=order_obj.to_dict()))
                buf_events.append(ClickstreamDB(event_json=evt))

            db.session.bulk_save_objects(buf_orders + buf_events)
            db.session.commit()
            LOGGER.info("Inserted %d + %d rows.", len(buf_orders), len(buf_events))
    except Exception:
        LOGGER.exception("add_new_combined_batch() failed.")


with app.app_context():
    init_db()
    maybe_init_data()

scheduler.add_job(add_new_combined_batch, "interval", seconds=NEW_BATCH_INTERVAL_SECONDS)
scheduler.start()

def _format_async_result(res: AsyncResult) -> Dict[str, Any]:
    """Turn an `AsyncResult` into a serialisable structure."""
    payload: Dict[str, Any] = {"task_id": res.id, "status": res.status}
    if res.successful():
        payload["result"] = res.result
    elif res.failed():
        payload["error"] = str(res.result)
    return payload


@app.route("/orders", methods=["GET"])
def get_orders():
    """Paginate stored orders (server‑side cached in Redis)."""
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 1_000))
    cache_key = f"orders:{page}:{limit}"
    if (cached := redis_client.get(cache_key)) is not None:
        return jsonify(json.loads(cached)), 200

    offset = (page - 1) * limit
    total = db.session.query(OrderDB).count()
    rows = (
        db.session.query(OrderDB).order_by(OrderDB.id).offset(offset).limit(limit).all()
    )

    response = {
        "page": page,
        "limit": limit,
        "total_orders": total,
        "total_pages": math.ceil(total / limit),
        "data": [r.order_json for r in rows],
    }
    redis_client.setex(cache_key, 60, json.dumps(response))
    return jsonify(response), 200


@app.route("/orders", methods=["POST"])
def create_order():
    """
    Generate a *single* order synchronously via the in‑process generator.

    Demonstrates explicit use of the `Order` domain object and
    `OrderStatusHistory` for an additional status marker.
    """
    new_order: Order = generator.generate_order()
    new_order.status_history.append(
        OrderStatusHistory("Created via API").to_dict()
    )

    db.session.add(OrderDB(order_json=new_order.to_dict()))
    db.session.commit()

    return (
        jsonify({"message": "Order created", "order_id": new_order.order_id}),
        201,
    )


@app.route("/clickstream", methods=["GET"])
def get_clickstream():
    """Paginate stored click‑stream rows (cached)."""
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 1_000))
    cache_key = f"clickstream:{page}:{limit}"
    if (cached := redis_client.get(cache_key)) is not None:
        return jsonify(json.loads(cached)), 200

    offset = (page - 1) * limit
    total = db.session.query(ClickstreamDB).count()
    rows = (
        db.session.query(ClickstreamDB)
        .order_by(ClickstreamDB.id)
        .offset(offset)
        .limit(limit)
        .all()
    )
    response = {
        "page": page,
        "limit": limit,
        "total_events": total,
        "total_pages": math.ceil(total / limit),
        "data": [r.event_json for r in rows],
    }
    redis_client.setex(cache_key, 60, json.dumps(response))
    return jsonify(response), 200


@app.route("/tasks/generate-orders", methods=["POST"])
def enqueue_generate_orders():
    """
    Enqueue an asynchronous *order* batch generation via Celery.

    Body JSON schema:
        { "count": <positive int> }
    """
    count = int(request.json.get("count", 10))
    res = generate_orders_task.delay(count)
    return jsonify({"task_id": res.id, "status": res.status}), 202


@app.route("/tasks/generate-clickstream", methods=["POST"])
def enqueue_generate_clickstream():
    """Same as above but for click‑stream events."""
    count = int(request.json.get("count", 10))
    res = generate_clickstream_task.delay(count)
    return jsonify({"task_id": res.id, "status": res.status}), 202


@app.route("/tasks/<task_id>", methods=["GET"])
def poll_task(task_id: str):
    """Poll a Celery task for completion / fetch its results."""
    res = AsyncResult(task_id, app=celery_app)
    return jsonify(_format_async_result(res)), (200 if res.ready() else 202)


@app.route("/coupon-usage", methods=["GET"])
def coupon_usage():
    """Return in‑memory coupon redemption count."""
    return jsonify(COUPON_USAGE), 200


@app.route("/health", methods=["GET"])
def health():
    """Liveness / readiness probe."""
    try:
        redis_client.ping()
        db.session.execute("SELECT 1")
        return jsonify({"status": "ok"}), 200
    except Exception as exc:
        return jsonify({"status": "unhealthy", "detail": str(exc)}), 500


@app.route("/")
def index():
    """Landing page."""
    return jsonify({"message": "Fake E‑commerce API is running"}), 200


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5001)
