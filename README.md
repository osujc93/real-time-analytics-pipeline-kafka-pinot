# **Real-Time Analytics Pipeline**

## Overview

This project is a real-time analytics pipeline that uses Apache Kafka, Apache Pinot, Quarkus and Streamlit. Order events are captured in Kafka topic, transformed and indexed in Pinot realtime table, rolling metrics computed via Kafka Streams in Quarkus, and Streamlit provides visualizations of these metrics.

## Architecture
The system consists of:

- **Flask REST API**: Generates online orders continuously in JSON.
- **Kafka**: 1 Controller & 3 brokers configured in KRaft mode. Kafka producer used to continuously fetch orders from API.
- **Pinot**: For real-time OLAP queries on data in Kafka topic. Pinot ingests events in real-time and applies JSON decoding and transformation into columns.
- **Quarkus**: Runs a Kafka Streams topology that reads from the topic; computing time-windowed aggregates (60s), and storing them in state stores. Also includes REST endpoints for queries against Pinot. Quarkus app then exposes these streaming aggregates & queries via HTTP endpoints. 
- **Zookeeper**: 3 Participants & 2 Observers used for Pinot's internal cluster management.
- **Postgres**: Backend for API & Airflow.
- **Streamlit**: Live dashboard. Calls the Quarkus HTTP endpoints and returns visualization of the metrics.
- **Airflow**: Automates entire workflow. DAG executes once all containers are up and running.

## Setup

### Prerequisites
- Docker & Docker Compose installed
- 
