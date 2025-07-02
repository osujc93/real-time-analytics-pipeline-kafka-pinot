from datetime import timedelta
import pendulum
from airflow import DAG
from ordersTasks import OrdersTasks

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

local_tz = pendulum.timezone("America/New_York")

with DAG(
    dag_id="Real-Time_Pipeline",
    default_args=default_args,
    description=(
        "Kafka + Pinot + Quarkus + Streamlit"
    ),
    schedule_interval="@weekly",
    start_date=pendulum.datetime(2024, 1, 1, tz=local_tz),
    catchup=False,
    is_paused_upon_creation=False,
    tags=["real-time", "orders"],
) as dag:

    start = OrdersTasks.start_task()

    orders_producer = OrdersTasks.orders_kafka_producer()

    pinot_add = OrdersTasks.pinot_add_tables()

    quarkus_run = OrdersTasks.quarkus_build_and_run()

    streamlit_run = OrdersTasks.streamlit_app_run()

    end = OrdersTasks.end_task()

    start >> [orders_producer, pinot_add, quarkus_run, streamlit_run] >> end
