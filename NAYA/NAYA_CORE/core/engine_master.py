# NAYA_CORE/core/engine_master.py

from typing import Dict, Any

from NAYA_CORE.decision.decision_core import DecisionCore
from NAYA_CORE.decision.execution_trigger import EXECUTION_TRIGGER


class EngineMaster:
    """
    Central orchestrator of NAYA.
    Does not decide.
    Does not execute directly.
    Coordinates decision and execution layers.
    """

    def __init__(self) -> None:
        self.decision_core = DecisionCore()

    def process(self, opportunity: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full industrial processing cycle:
        1. Decision phase
        2. Execution phase (if approved)
        """

        # ---- Phase 1: Decision ----
        decision_result: Dict[str, Any] = self.decision_core.evaluate(opportunity)

        # If not approved, stop immediately
        if decision_result.get("status") != "APPROVED":
            return decision_result

        # ---- Phase 2: Execution ----
        execution_result: Dict[str, Any] = EXECUTION_TRIGGER.trigger(decision_result)

        return execution_result
