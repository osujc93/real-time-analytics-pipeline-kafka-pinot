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
- 32gb of memory

### Deployment
1. Clone repository:
   ```sh
   $ git clone <repository-url>
   $ cd real-time-analytics-pipeline-kafka-pinot
   ```

2. Build and start services:
   ```sh
   $ docker-compose build

   $ docker-compose up -d
   ```

3. 
   ```sh

   ```
   
## Pinot Queries & Examples of Outputs from Endpoints:

http://localhost:8888/orders/overview

Endpoint for Kafka Streams topology that keeps rolling 1-second-advancing, 60-second windows of key business metrics.

Everything is persisted in embedded RocksDB state stores so the data can be queried on demand without hitting Pinot/PostgreSQL.

```sh

@ApplicationScoped
public class OrdersTopology {

    @Produces
    public Topology buildTopology() {

        final Serde<Order>    orderSerde  = Serdes.serdeFrom(new JsonSerializer<>(), new JsonDeserializer<>(Order.class));
        final Serde<String>   stringSerde = Serdes.String();
        final Serde<Integer>  intSerde    = Serdes.Integer();

        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, Order> orders =
                builder.stream("FakeEcommOrders", Consumed.with(Serdes.String(), orderSerde));

        TimeWindows timeWindow = TimeWindows
                .ofSizeAndGrace(Duration.ofSeconds(60), Duration.ofMinutes(5))
                .advanceBy(Duration.ofSeconds(1));

        orders.groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("OrdersCountStore"));

        orders.groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .aggregate(() -> 0.0,
                         (k, v, agg) -> agg + v.order_total,
                         Materialized.<String, Double, WindowStore<Bytes, byte[]>>as("RevenueStore")
                                     .withValueSerde(Serdes.Double()));

        orders.filter((k, v) -> v != null && isFraud(v))
              .groupBy((k, v) -> "fraud", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("FraudCountStore"));

        orders.filter((k, v) -> v != null && "yes".equalsIgnoreCase(v.delivered))
              .groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("DeliveredCountStore"));

        orders.filter((k, v) -> v != null && "yes".equalsIgnoreCase(v.refunded))
              .groupBy((k, v) -> "count", Grouped.with(stringSerde, orderSerde))
              .windowedBy(timeWindow)
              .count(Materialized.as("RefundedCountStore"));

        return builder.build();
    }
}

```

![Diagram](/images/pinot-data-1.png)

http://localhost:8888/orders/overview2

```sh

-- Rreturns the number of distinct orders, sum of order_total, and separate
-- counts of orders that were refunded, delivered, or flagged as fraud
-- for the most recent 60 seconds and for the previous 60 seconds.

SELECT
  COUNT(DISTINCT order_id) FILTER (WHERE time_ms > ago('PT1M'))                                                       AS events1Min,
  COUNT(DISTINCT order_id) FILTER (WHERE time_ms <= ago('PT1M') AND time_ms > ago('PT2M'))                            AS events1Min2Min,
  SUM(DISTINCT order_total) FILTER (WHERE time_ms > ago('PT1M'))                                                      AS total1Min,
  SUM(DISTINCT order_total) FILTER (WHERE time_ms <= ago('PT1M') AND time_ms > ago('PT2M'))                           AS total1Min2Min,
  COUNT(DISTINCT order_id) FILTER (WHERE refunded  = 'yes' AND time_ms > ago('PT1M'))                                 AS refunded_events_1min,
  COUNT(DISTINCT order_id) FILTER (WHERE delivered = 'yes' AND time_ms > ago('PT1M'))                                 AS deliver_events_1min,
  COUNT(DISTINCT order_id) FILTER (WHERE fraud_flag = TRUE  AND time_ms > ago('PT1M'))                                AS fraud_events_1min,
  COUNT(DISTINCT order_id) FILTER (WHERE refunded  = 'yes' AND time_ms <= ago('PT1M') AND time_ms > ago('PT2M'))      AS refunded_events_2min,
  COUNT(DISTINCT order_id) FILTER (WHERE delivered = 'yes' AND time_ms <= ago('PT1M') AND time_ms > ago('PT2M'))      AS delivered_events_2min,
  COUNT(DISTINCT order_id) FILTER (WHERE fraud_flag = TRUE  AND time_ms <= ago('PT1M') AND time_ms > ago('PT2M'))     AS fraud_events_2min
FROM orders;

```

http://localhost:8888/orders/popular

```sh

-- Top 5 Products Ordered In the Last Minute

SELECT line_items.product.name            AS itemName,  
COUNT(DISTINCT order_id)                  AS orders, 
SUMMV(line_items.quantity)                AS quantity 
FROM orders WHERE time_ms > ago('PT1M') 
GROUP BY line_items.product.name      
ORDER BY quantity DESC LIMIT 5;

-- Top 5 Categories of Products Ordered In the Last Minute

SELECT line_items.product.category        AS category,  
COUNT(DISTINCT order_id)                  AS orders, 
SUMMV(line_items.quantity)                AS quantity 
FROM orders 
WHERE time_ms > ago('PT1M') 
GROUP BY line_items.product.category  
ORDER BY quantity DESC LIMIT 5;

```

http://localhost:8888/orders/ordersperminute

```sh

--

SELECT ToDateTime(DATETRUNC('MINUTE',time_ms,'MILLISECONDS'),'yyyy-MM-dd HH:mm:ss','America/New_York') AS dateMin, 
COUNT(DISTINCT order_id)                                        AS orders, 
SUM(DISTINCT order_total)                                       AS totalRev, 
COUNT(DISTINCT order_id) FILTER (WHERE fraud_flag='true')       AS fraudCount, 
COUNT(DISTINCT order_id) FILTER (WHERE delivered='yes')         AS deliveredCount, 
COUNT(DISTINCT order_id) FILTER (WHERE refunded='yes')          AS refundedCount 
FROM orders 
WHERE time_ms>ago('PT1H') 
GROUP BY dateMin 
ORDER BY dateMin 
LIMIT 60;

```

http://localhost:8888/orders/latestorders

```sh

--

SELECT order_id, 
ToDateTime(MAX(time_ms),'yyyy-MM-dd HH:mm:ss','America/New_York') AS time_ny, 
MAX(order_total)			AS order_total, 
customer_id, 
MAX(productsOrdered)		        AS productsOrdered, 
MAX(totalQuantity)			AS totalQuantity 
FROM orders 
GROUP BY order_id, customer_id 
ORDER BY time_ny 
DESC LIMIT 10;

```


## Streamlit

http://localhost:8501

![Diagram](/images/dashboard1.png)

![Diagram](/images/dashboard2.png)

