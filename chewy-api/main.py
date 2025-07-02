from __future__ import annotations

import json
import logging
import math
import os
from typing import Any, Dict, List

import redis
import sqlalchemy as sa
from apscheduler.schedulers.background import BackgroundScheduler
from celery.result import AsyncResult
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from promotions import COUPON_USAGE
from location_data import USZipcodeLocationData
from order import Order
from order_status_history import OrderStatusHistory
from celery_worker import celery_app, generate_clickstream_task, generate_orders_task
from data_model import FakeEcommerceDataGenerator

# ─────────────────────────  LOGGING  ──────────────────────────
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
LOGGER = logging.getLogger(__name__)

# ─────────────────────────  CONSTANTS  ─────────────────────────
FAKE_RECORD_COUNT = int(os.getenv("FAKE_RECORD_COUNT", 1111))
NEW_BATCH_SIZE = int(os.getenv("NEW_BATCH_SIZE", 777))
NEW_BATCH_INTERVAL_SECONDS = int(os.getenv("NEW_BATCH_INTERVAL_SECONDS", 25))

FAKE_CLICKSTREAM_COUNT = int(os.getenv("FAKE_CLICKSTREAM_COUNT", 1111))
NEW_CLICKSTREAM_BATCH_SIZE = int(os.getenv("NEW_CLICKSTREAM_BATCH_SIZE", 777))

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "blewy")
POSTGRES_USER = os.getenv("POSTGRES_USER", "blewy")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Password123456789")

# psycopg-v3 driver
DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:5432/{POSTGRES_DB}",
)

POOL_SIZE = int(os.getenv("SQLALCHEMY_POOL_SIZE", 10))
POOL_TIMEOUT = int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", 30))

# ─────────────────────────  FLASK / DB  ────────────────────────
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": POOL_SIZE,
    "pool_timeout": POOL_TIMEOUT,
    "pool_recycle": 1800,  # recycle idle conns every 30 min
    "max_overflow": 5,
}
db = SQLAlchemy(app)

# helper: always return the connection to the pool
def _commit_and_close() -> None:
    db.session.commit()
    db.session.close()

# ─────────────────────────  MODELS  ────────────────────────────
class OrderDB(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_json = db.Column(db.JSON, nullable=False)


class ClickstreamDB(db.Model):
    __tablename__ = "clickstream"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_json = db.Column(db.JSON, nullable=False)


# ─────────────────────────  GLOBALS  ───────────────────────────
redis_client = redis.Redis(host="redis", port=6379, db=0, socket_connect_timeout=2)
generator = FakeEcommerceDataGenerator()
scheduler = BackgroundScheduler()

# ─────────────────────  DB-INIT / SEED  ────────────────────────
def init_db() -> None:
    with app.app_context():
        if {"orders", "clickstream"} <= set(sa.inspect(db.engine).get_table_names()):
            LOGGER.info("Tables present – skipping creation.")
            return
        db.create_all()
        LOGGER.info("Tables created - orders, clickstream.")


def init_combined_data() -> None:
    try:
        target = min(FAKE_RECORD_COUNT, FAKE_CLICKSTREAM_COUNT)
        if target <= 0:
            LOGGER.info("No seed-data requested (target <= 0).")
            return

        USZipcodeLocationData.init_uszipcode_data()
        chunk = 1_000
        buf_orders, buf_events = [], []

        LOGGER.info("Generating %d synthetic orders + events …", target)
        for idx in range(target):
            cust = generator.generate_customer_info()
            buf_orders.append(
                OrderDB(order_json=generator.generate_order(customer=cust).to_dict())
            )
            buf_events.append(
                ClickstreamDB(
                    event_json=generator.generate_clickstream_event(customer=cust)
                )
            )

            if (idx + 1) % chunk == 0:
                db.session.bulk_save_objects(buf_orders + buf_events)
                _commit_and_close()
                LOGGER.debug("Inserted %d / %d rows …", idx + 1, target)
                buf_orders.clear()
                buf_events.clear()

        if buf_orders:
            db.session.bulk_save_objects(buf_orders + buf_events)
            _commit_and_close()

        LOGGER.info("Seed generation complete (%d pairs).", target)
    except Exception:  # pragma: no cover
        LOGGER.exception("init_combined_data() - unrecoverable error.")
        db.session.rollback()
        db.session.close()


def maybe_init_data() -> None:
    with app.app_context():
        if db.session.query(OrderDB).count() == 0 or db.session.query(
            ClickstreamDB
        ).count() == 0:
            init_combined_data()
        else:
            LOGGER.info("DB already seeded - skipping.")
        db.session.close()


# ─────────────────────  BACKGROUND JOB  ────────────────────────
def add_new_combined_batch() -> None:
    try:
        with app.app_context():
            batch = min(NEW_BATCH_SIZE, NEW_CLICKSTREAM_BATCH_SIZE)
            if batch <= 0:
                LOGGER.debug("Batch size <= 0 - nothing to add.")
                return

            LOGGER.info("Appending %d new order/event pairs …", batch)
            buf_orders, buf_events = [], []

            for _ in range(batch):
                cust = generator.generate_customer_info()
                buf_orders.append(
                    OrderDB(order_json=generator.generate_order(customer=cust).to_dict())
                )
                buf_events.append(
                    ClickstreamDB(
                        event_json=generator.generate_clickstream_event(customer=cust)
                    )
                )

            db.session.bulk_save_objects(buf_orders + buf_events)
            _commit_and_close()
            LOGGER.info("Inserted %d + %d rows.", len(buf_orders), len(buf_events))
    except Exception:  # pragma: no cover
        LOGGER.exception("add_new_combined_batch() failed.")
        db.session.rollback()
        db.session.close()


# ─────────────────────  START-UP SEQUENCE  ─────────────────────
with app.app_context():
    init_db()
    maybe_init_data()

scheduler.add_job(add_new_combined_batch, "interval", seconds=NEW_BATCH_INTERVAL_SECONDS)
scheduler.start()

# ─────────────────────  HELPERS  ───────────────────────────────
def _format_async_result(res: AsyncResult) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"task_id": res.id, "status": res.status}
    if res.successful():
        payload["result"] = res.result
    elif res.failed():
        payload["error"] = str(res.result)
    return payload


# ─────────────────────  ROUTES  ────────────────────────────────
@app.route("/orders", methods=["GET"])
def get_orders():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 1_000))
    offset = (page - 1) * limit
    cache_key = f"orders:{page}:{limit}"

    cached = redis_client.get(cache_key)
    if cached:
        return jsonify(json.loads(cached)), 200

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
    new_order: Order = generator.generate_order()
    new_order.status_history.append(OrderStatusHistory("Created via API").to_dict())
    db.session.add(OrderDB(order_json=new_order.to_dict()))
    _commit_and_close()
    return jsonify({"message": "Order created", "order_id": new_order.order_id}), 201


@app.route("/clickstream", methods=["GET"])
def get_clickstream():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 1_000))
    offset = (page - 1) * limit
    cache_key = f"clickstream:{page}:{limit}"

    cached = redis_client.get(cache_key)
    if cached:
        return jsonify(json.loads(cached)), 200

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


# Celery task endpoints -------------------------------------------------------
@app.route("/tasks/generate-orders", methods=["POST"])
def enqueue_generate_orders():
    res = generate_orders_task.delay(int(request.json.get("count", 10)))
    return jsonify({"task_id": res.id, "status": res.status}), 202


@app.route("/tasks/generate-clickstream", methods=["POST"])
def enqueue_generate_clickstream():
    res = generate_clickstream_task.delay(int(request.json.get("count", 10)))
    return jsonify({"task_id": res.id, "status": res.status}), 202


@app.route("/tasks/<task_id>", methods=["GET"])
def poll_task(task_id: str):
    res = AsyncResult(task_id, app=celery_app)
    return jsonify(_format_async_result(res)), (200 if res.ready() else 202)


# ─────────────────────  HEALTH CHECK  ─────────────────────────
@app.route("/health", methods=["GET"])
def health():
    try:
        redis_client.ping()
        # short-lived, independent DB connection
        with db.engine.connect() as conn:
            conn.execute(sa.text("SELECT 1"))
        return jsonify({"status": "ok"}), 200
    except Exception as exc:  # pragma: no cover
        LOGGER.exception("Health check failed")
        return jsonify({"status": "unhealthy", "detail": str(exc)}), 500


@app.route("/")
def index():
    return jsonify({"message": "Fake E-commerce API is running"}), 200


# ─────────────────────  MAIN  ──────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
