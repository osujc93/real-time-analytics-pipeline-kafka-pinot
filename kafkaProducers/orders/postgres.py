#!/usr/bin/env python3

from __future__ import annotations

import psycopg2
from psycopg2.extensions import connection, cursor

from configs import logger


class PostgresClient:

    def __init__(
        self,
        dsn: str = "dbname=blewy user=blewy password=Password123456789 host=postgres port=5432",
    ) -> None:
        self._dsn = dsn
        self._conn: connection | None = None

    def __enter__(self) -> cursor:
        self._conn = psycopg2.connect(self._dsn)
        self._conn.autocommit = True
        return self._conn.cursor()

    def __exit__(self, exc_type, exc, tb) -> None:
        if self._conn:
            self._conn.close()


def finalize_ingestion_metadata() -> None:
    sql_setup = """
        CREATE TABLE IF NOT EXISTS ecommerce_ingestion_metadata (
            id SERIAL PRIMARY KEY,
            last_ingestion_timestamp TIMESTAMP NOT NULL
                DEFAULT CURRENT_TIMESTAMP
        );
    """
    sql_insert = "INSERT INTO ecommerce_ingestion_metadata DEFAULT VALUES;"

    try:
        with PostgresClient() as cur:
            cur.execute(sql_setup)
            cur.execute(sql_insert)
            logger.info("Postgres ingestion metadata updated.")
    except Exception as err:
        logger.error("Postgres error: %s", err)
