#!/usr/bin/env python3
"""
config.py – Centralised configuration helpers.
Sets up logging and Kafka producer/admin parameters.
"""
from __future__ import annotations

import json
import logging
from typing import Dict, List, Union

from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

def get_logger(name: str = "orders_producer") -> logging.Logger:
    """Return a module‑level logger configured for DEBUG verbosity."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(name)

logger = get_logger()

BOOTSTRAP_SERVERS: List[str] = [
    "172.20.10.2:9092",
    "172.20.10.3:9093",
    "172.20.10.4:9094",
]

_PRODUCER_CONFIG: Dict[str, Union[str, int]] = {
    "bootstrap_servers": BOOTSTRAP_SERVERS,
    "value_serializer": lambda x: json.dumps(x).encode("utf-8"),
    "key_serializer": lambda x: str(x).encode("utf-8"),
    "retries": 10,
    "max_block_ms": 120_000,
    "request_timeout_ms": 120_000,
    "acks": "all",
    "linger_ms": 0,
    "batch_size": 5 * 1024 * 1024,
    "max_request_size": 20 * 1024 * 1024,
    "compression_type": "snappy",
    "buffer_memory": 512 * 1024 * 1024,
    "max_in_flight_requests_per_connection": 5,
}

class KafkaConfig:
    """Factory helpers for Kafka‑related objects."""

    @staticmethod
    def producer() -> KafkaProducer:
        """Return a fully‑configured :class:`KafkaProducer`."""
        return KafkaProducer(**_PRODUCER_CONFIG)

    @staticmethod
    def create_topic(
        topic_name: str, num_partitions: int = 24, replication_factor: int = 3
    ) -> None:
        """Idempotently create a topic if it does not yet exist."""
        admin = KafkaAdminClient(
            bootstrap_servers=BOOTSTRAP_SERVERS, client_id="FakeEcommOrders"
        )
        topic = NewTopic(
            name=topic_name,
            num_partitions=num_partitions,
            replication_factor=replication_factor,
        )

        try:
            if topic_name not in admin.list_topics():
                admin.create_topics([topic])
                logger.info(
                    "Created topic '%s' (partitions=%d, rf=%d)",
                    topic_name,
                    num_partitions,
                    replication_factor,
                )
        except TopicAlreadyExistsError:
            logger.debug("Topic '%s' already exists – OK", topic_name)
        finally:
            admin.close()
