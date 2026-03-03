# workflow_runtime.py

from workflow_registry import WORKFLOWS


class WorkflowRuntime:

    def __init__(self, action_engine, retry_policy, state_manager):
        self.action_engine = action_engine
        self.retry_policy = retry_policy
        self.state_manager = state_manager

    def run(self, workflow_name: str, context: dict):

        workflow = WORKFLOWS.get(workflow_name)

        if not workflow:
            raise Exception("Workflow not found")

        for step in workflow["steps"]:

            method = getattr(self.action_engine, step)

            context = self.retry_policy.execute(method, context)

            self.state_manager.set("last_step", step)

        return context
