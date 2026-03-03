"""
Cartographie des besoins non exprimés.
Aucune exécution. Déclaratif.
"""

def get_unspoken_needs_signals() -> dict:
    return {
        "type": "UNSPOKEN_NEEDS",
        "description": "Besoins réels non formulés publiquement",
        "signals": [
            "contournements récurrents",
            "silence prolongé malgré douleur",
            "acceptation résignée",
            "solutions artisanales persistantes"
        ],
        "decision_role": "NON_DECISIONNAIRE"
    }
