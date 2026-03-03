"""
Zones de silence institutionnel.
"""

def identify_silence_zones() -> dict:
    return {
        "type": "INSTITUTIONAL_SILENCE",
        "description": "Problèmes connus mais volontairement tus",
        "zones": [
            "process intouchables",
            "coûts normalisés",
            "équipes sous pression invisible"
        ],
        "decision_role": "NON_DECISIONNAIRE"
    }
