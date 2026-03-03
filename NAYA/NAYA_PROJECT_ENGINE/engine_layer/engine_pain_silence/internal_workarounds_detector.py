"""
Détection des contournements internes.
Analyse déclarative des signaux faibles.
"""

def detect_internal_workarounds() -> dict:
    return {
        "type": "INTERNAL_WORKAROUNDS",
        "description": "Solutions officieuses mises en place faute de solution formelle",
        "signals": [
            "tableurs non officiels",
            "scripts personnels",
            "prestataires non référencés",
            "process parallèles",
            "outils tolérés mais non documentés"
        ],
        "interpretation": "UNMET_NEED",
        "visibility": "LOW",
        "decision_role": "NON_DECISIONNAIRE"
    }
