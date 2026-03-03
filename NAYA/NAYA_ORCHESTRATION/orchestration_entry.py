from NAYA_ORCHESTRATION.core.execution_request import ExecutionRequest
from NAYA_ORCHESTRATION.router.environment_router import EnvironmentRouter
from NAYA_ORCHESTRATION.executors.vm_executor import VMExecutor
from NAYA_ORCHESTRATION.executors.cloudrun_executor import CloudRunExecutor
from NAYA_ORCHESTRATION.monitoring.execution_logger import ExecutionLogger

class OrchestrationEntry:

    def __init__(self):
        self.logger = ExecutionLogger()
        self.router = EnvironmentRouter({
            "vm": {"cost":0.3,"density":0.6,"performance":0.7},
            "cloudrun": {"cost":0.5,"density":0.9,"performance":0.85}
        })
        self.executors = {
            "vm": VMExecutor(),
            "cloudrun": CloudRunExecutor()
        }

    def execute(self, directive_id: str, payload: dict, economic_weight: float):
        env = self.router.select(economic_weight)
        self.logger.log(f"Selected environment: {env}")
        result = self.executors[env].execute(payload)
        self.logger.log(f"Execution complete for {directive_id}")
        return result