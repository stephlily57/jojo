# NAYA_CORE/decision/decision_core.py

from typing import Dict, Any

from NAYA_CORE.economic.capital_reserve_manager import CAPITAL_RESERVE_MANAGER
from NAYA_CORE.doctrine.economic_thresholds import EconomicThresholds
from NAYA_CORE.doctrine.core_constitution import CoreConstitution


class DecisionCore:
    """
    Strategic Decision Layer.
    Responsible ONLY for evaluating and producing
    a structured decision payload.
    """

    def evaluate(self, opportunity: Dict[str, Any]) -> Dict[str, Any]:

        if not opportunity:
            return {
                "status": "REJECTED",
                "reason": "EMPTY_OPPORTUNITY"
            }

        project_id: str = opportunity.get("name", "UNKNOWN_PROJECT")
        value: float = float(opportunity.get("value", 0))

        # ---- Capital validation ----
        if not CAPITAL_RESERVE_MANAGER.can_allocate(value):
            return {
                "status": "REJECTED",
                "reason": "CAPITAL_LIMIT_EXCEEDED"
            }

        # ---- Economic classification ----
        classification: str = EconomicThresholds.classify(value)

        if classification == "REJECT":
            return {
                "status": "REJECTED",
                "reason": "BELOW_STRATEGIC_THRESHOLD"
            }

        # ---- Density computation ----
        density: float = round(value / 100000, 4) if value else 0.0

        # ---- Strategic mode ----
        if value >= 75000:
            mode: str = "INDUSTRIAL"
        elif value >= 25000:
            mode: str = "ACCELERATION"
        else:
            mode: str = "STANDARD"

        # ---- Final decision payload ----
        decision_payload: Dict[str, Any] = {
            "project_id": project_id,
            "capital_allocated": value,
            "classification": classification,
            "mode": mode,
            "density": density,
            "constitution_hash": CoreConstitution.integrity_hash()
        }

        return {
            "status": "APPROVED",
            "decision": decision_payload
        }
