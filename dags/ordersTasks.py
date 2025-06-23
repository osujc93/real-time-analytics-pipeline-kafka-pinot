import os
from typing import Any
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from dagUtils import DockerOperatorWithCleanup


class OrdersTasks:
    """
    A static utility class to build tasks for the DAG.

    Each method returns an Airflow Operator instance representing a step
    (BashOperator, DockerOperatorWithCleanup, etc.).
    """

    @staticmethod
    def start_task() -> EmptyOperator:
        """
        Create an EmptyOperator to mark the start of the DAG.
        """
        return EmptyOperator(task_id="start")

    @staticmethod
    def do_initial_chain() -> EmptyOperator:
        """
        Create an EmptyOperator marking the start of the initial ingestion chain.
        """
        return EmptyOperator(task_id="do_initial_chain")

    @staticmethod
    def skip_initial_chain() -> EmptyOperator:
        """
        Create an EmptyOperator marking a skip of the initial chain.
        """
        return EmptyOperator(task_id="skip_initial_chain")

    @staticmethod
    def end_task() -> EmptyOperator:
        """
        Create an EmptyOperator to mark the end of the DAG.
        """
        return EmptyOperator(task_id="end")

    @staticmethod
    def orders_kafka_producer() -> BashOperator:
        """
        Create a BashOperator to run the 'orders' Kafka producer Python script.
        """
        return BashOperator(
            task_id="orders_kafka_producer",
            bash_command=(
                "python3 /opt/airflow/kafkaProducers/orders/main.py"
            ),
        )

    @staticmethod
    def pinot_add_tables() -> DockerOperatorWithCleanup:
        """
        DockerOperator to Add the Clickstreams and Orders tables/schemas to Pinot
        after a 30-second delay.
        """
        return DockerOperatorWithCleanup(
            task_id="pinot_add_tables",
            image="pinot-controller:latest",
            container_name="pinot_add_tables_container",
            entrypoint="/bin/bash",
            command=(
                "-c 'sleep 220 && "
                "/opt/pinot/bin/pinot-admin.sh AddTable "
                "-schemaFile /opt/pinot/conf/orders/schema.json "
                "-tableConfigFile /opt/pinot/conf/orders/table.json "
                "-controllerHost pinot-controller "
                "-controllerPort 9000 "
                "-exec'"
            ),
            network_mode="nelo-data-pipeline",
            docker_url="unix://var/run/docker.sock",
            mount_tmp_dir=False,
            api_version="auto",
            auto_remove=True
        )

    @staticmethod
    def quarkus_build_and_run() -> BashOperator:
        """
        Create a BashOperator to build and run the quarkus java app.
        """
        return BashOperator(
            task_id="quarkus_build_and_run",
            bash_command="""
                cd /opt/airflow/blewy &&
                quarkus build --no-tests -Dquarkus.package.type=uber-jar &&
                java -jar /opt/airflow/blewy/target/blewy-0.0.1-runner.jar > quarkus.log 2>&1
            """,
        )

    @staticmethod
    def streamlit_app_run() -> BashOperator:
        """
        Create a BashOperator to run the streamlit Python script.
        """
        return BashOperator(
            task_id="streamlit_app_run",
            bash_command="""
                sleep 400 &&
                cd /opt/airflow &&
                streamlit run /opt/airflow/app.py
            """,
        )