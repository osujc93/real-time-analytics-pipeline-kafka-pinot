#!/usr/bin/env python3
"""
main.py – Entry‑point script.
Launches :class:`OrderIngestion` and blocks forever.
"""
from ingestion import OrderIngestion

if __name__ == "__main__":
    OrderIngestion(topic="FakeEcommOrders").run_forever()
