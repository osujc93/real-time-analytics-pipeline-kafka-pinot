#!/usr/bin/env python3

from ingestion import OrderIngestion

if __name__ == "__main__":
    OrderIngestion(topic="FakeEcommOrders").run_forever()
