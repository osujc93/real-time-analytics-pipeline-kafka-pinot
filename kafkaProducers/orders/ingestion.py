#!/usr/bin/env python3
"""
ingestion.py – Pulls pages from the fake API and publishes to Kafka.
"""

from __future__ import annotations

import time
from datetime import datetime, timezone
from typing import Optional

import pytz
import requests
from kafka.errors import KafkaTimeoutError, NotLeaderForPartitionError
from kafka.producer import KafkaProducer
from pydantic import ValidationError

from configs import KafkaConfig, logger
from pydanticModels import EcommOrder, OrdersApiResponse
from postgres import finalize_ingestion_metadata

NY_TZ = pytz.timezone("America/New_York")


class OrderIngestion:
    """High‑level orchestrator that streams orders into Kafka."""

    def __init__(self, topic: str = "FakeEcommOrders") -> None:
        self.topic = topic
        self.producer: KafkaProducer = KafkaConfig.producer()
        KafkaConfig.create_topic(topic)

    @staticmethod
    def _now_str() -> str:
        """Current NY timestamp with millisecond precision."""
        return datetime.now(NY_TZ).strftime("%Y-%m-%dT%H:%M:%S.%f")

    @staticmethod
    def _now_ms() -> int:
        """Unix epoch milliseconds (UTC)."""
        return int(datetime.now(timezone.utc).timestamp() * 1000)
    
    @staticmethod
    def _fetch_page(page: int, session: requests.Session) -> Optional[OrdersApiResponse]:
        url = f"http://fake-ecommerce-api:5001/orders?page={page}"
        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()
            return OrdersApiResponse(**response.json())
        except (requests.RequestException, ValidationError) as err:
            logger.error("Fetch/validation error for page %d: %s", page, err)
            return None

    # --------------------------------------------------------------------- #
    # Main loop
    # --------------------------------------------------------------------- #
    def run_forever(self) -> None:
        """Continuously pull pages and publish records."""
        page = 1
        session = requests.Session()

        try:
            while True:
                api_page = self._fetch_page(page, session)
                if api_page is None:  # back‑off then retry same page
                    time.sleep(5)
                    continue

                for order in api_page.data:
                    self._publish(order)

                logger.info(
                    "Page=%d | sent %d orders | topic=%s",
                    page,
                    len(api_page.data),
                    self.topic,
                )

                # round‑robin pagination
                page = 1 if page >= api_page.total_pages else page + 1
        except KeyboardInterrupt:
            logger.info("Interrupted – shutting down.")
        finally:
            finalize_ingestion_metadata()
            self.producer.close()

    # --------------------------------------------------------------------- #
    # Internal publishing
    # --------------------------------------------------------------------- #
    def _publish(self, order: EcommOrder) -> None:
        msg = order.model_dump()
        msg["timestamp"] = self._now_str()  
        
        msg["time_ms"]  = self._now_ms()

        try:
            self.producer.send(self.topic, key=order.order_id, value=msg)
        except (NotLeaderForPartitionError, KafkaTimeoutError) as err:
            logger.error("Kafka error (order %s): %s", order.order_id, err)
        except Exception as exc:
            logger.error("Unexpected error (order %s): %s", order.order_id, exc)
        else:
            # fire‑and‑forget for low latency; flush periodically
            self.producer.flush()
