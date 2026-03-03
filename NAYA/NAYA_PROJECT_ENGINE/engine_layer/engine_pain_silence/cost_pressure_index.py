"""
Indice de pression financière.
"""

def cost_pressure_index(cost_level: int, recurrence: int) -> dict:
    return {
        "index": cost_level * recurrence,
        "state": "MEASURED",
        "decision_role": "NON_DECISIONNAIRE"
    }
