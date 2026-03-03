"""
Marchés nécessitant discrétion absolue.
"""

def discretion_profile() -> dict:
    return {
        "visibility": "LOW",
        "confidentiality": "HIGH",
        "communication": "RESTRICTED",
        "decision_role": "CONDITIONED"
    }
