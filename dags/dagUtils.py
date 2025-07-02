import docker
from typing import Any, Dict
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.models import Variable

class DockerOperatorWithCleanup(DockerOperator):

    def execute(self, context: Dict[str, Any]) -> Any:
        if self.container_name:
            self._remove_existing_container(self.container_name)
        return super().execute(context)

    def _remove_existing_container(self, container_name: str) -> None:
        client = docker.from_env()
        try:
            container = client.containers.get(container_name)
            container.remove(force=True)
            print(f"Removed existing container: {container_name}")
        except docker.errors.NotFound:
            print(f"No existing container found with name: {container_name}")

class BranchDecider:

    @staticmethod
    def decide_initial_or_incremental() -> str:

        flag = Variable.get("init_ingestion_done", default_var="False")
        if flag.lower() == "true":
            return "skip_initial_chain"
        return "do_initial_chain"
