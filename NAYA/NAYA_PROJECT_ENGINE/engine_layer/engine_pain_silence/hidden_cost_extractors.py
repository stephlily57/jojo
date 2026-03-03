"""
Extraction déclarative des coûts cachés.
"""

def extract_hidden_costs() -> dict:
    return {
        "type": "HIDDEN_COSTS",
        "metrics": [
            "temps perdu",
            "énergie humaine",
            "complexité inutile",
            "friction organisationnelle"
        ],
        "decision_role": "NON_DECISIONNAIRE"
    }
