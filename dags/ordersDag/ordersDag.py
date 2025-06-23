"""
DAG definition for Orders Stats workflow.
"""

from datetime import timedelta
import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule

from dagUtils import BranchDecider
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
    dag_id="Orders_Stats_WorkFlow_OOP",
    default_args=default_args,
    description=(
        "End-to-end workflow: ingestion + Pinot + Quarkus + Streamlit"
    ),
    schedule_interval="@daily",
    start_date=pendulum.datetime(2024, 1, 1, tz=local_tz),
    catchup=False,
    is_paused_upon_creation=False,
    tags=["etl", "orders"],
) as dag:

    # 1) Start
    start = OrdersTasks.start_task()

    # 2) Run Kafka producers in parallel
    orders_producer = OrdersTasks.orders_kafka_producer()

    # 3) Pinot AddTable
    pinot_add = OrdersTasks.pinot_add_tables()

    # 4) Quarkus build + run
    quarkus_run = OrdersTasks.quarkus_build_and_run()

    # 5) Streamlit app run
    streamlit_run = OrdersTasks.streamlit_app_run()

    # 6) End
    end = OrdersTasks.end_task()

    # Define the sequence/parallelism:
    start >> [orders_producer, pinot_add, quarkus_run, streamlit_run] >> end
