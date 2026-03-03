# NAYA_CORE/decision/execution_trigger.py

from typing import Dict, Any
from NAYA_CORE.decision.project_engine_bridge import ProjectEngineBridge


class ExecutionTrigger:
    """
    Execution Gateway.
    Receives approved decision payload and
    launches the Project Engine.
    """

    def __init__(self) -> None:
        self.bridge = ProjectEngineBridge()

    def trigger(self, decision_result: Dict[str, Any]) -> Dict[str, Any]:

        if decision_result.get("status") != "APPROVED":
            return decision_result

        payload: Dict[str, Any] = decision_result.get("decision")

        if not payload:
            return {
                "status": "ERROR",
                "reason": "MISSING_DECISION_PAYLOAD"
            }

        project_response = self.bridge.launch_project(payload)

        return {
            "status": "EXECUTED",
            "project_response": project_response,
            "constitution_hash": payload.get("constitution_hash")
        }


EXECUTION_TRIGGER = ExecutionTrigger()
