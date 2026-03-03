"""
Cartographie des asymétries de pouvoir.
Analyse structurelle, non exécutive.
"""

def map_power_asymmetry() -> dict:
    return {
        "type": "POWER_ASYMMETRY",
        "description": "Situations où une partie détient un pouvoir disproportionné",
        "indicators": [
            "dépendance économique unilatérale",
            "absence d’alternative réaliste",
            "pression implicite",
            "acceptation contrainte"
        ],
        "affected_actors": [
            "employés",
            "prestataires",
            "freelances",
            "clients captifs",
            "sous-traitants"
        ],
        "risk_level": "SENSITIVE",
        "decision_role": "NON_DECISIONNAIRE"
    }
