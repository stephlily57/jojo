"""
Classification des niveaux de risque marché.
Déclaratif, non exécutoire.
"""

def market_risk_tiers() -> dict:
    return {
        "type": "MARKET_RISK_TIERS",
        "tiers": {
            "TIER_0": {
                "label": "INSTITUTIONAL",
                "description": "Marché propre, normé, public",
                "visibility": "HIGH",
                "risk": "LOW"
            },
            "TIER_1": {
                "label": "AGGRESSIVE_BUT_CLEAN",
                "description": "Marché concurrentiel, pression élevée",
                "visibility": "MEDIUM",
                "risk": "MEDIUM"
            },
            "TIER_2": {
                "label": "SENSITIVE",
                "description": "Marché délicat, nécessitant discrétion",
                "visibility": "LOW",
                "risk": "MEDIUM_HIGH"
            },
            "TIER_3": {
                "label": "HOSTILE",
                "description": "Environnement dur, asymétrique",
                "visibility": "VERY_LOW",
                "risk": "HIGH"
            },
            "TIER_4": {
                "label": "SURVIVAL",
                "description": "Marché de survie économique",
                "visibility": "MINIMAL",
                "risk": "CRITICAL"
            }
        },
        "decision_role": "NON_DECISIONNAIRE"
    }
