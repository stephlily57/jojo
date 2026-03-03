"""
Simulation d’impact sans exécution.
"""

def simulate_impact(benefit: int, risk: int) -> dict:
    return {
        "net_value": benefit - risk,
        "executed": False
    }
