"""
Registre des douleurs latentes observées.
"""

def register_latent_pain(pain_id: str, context: str) -> dict:
    return {
        "pain_id": pain_id,
        "context": context,
        "state": "OBSERVED",
        "action": "NONE"
    }
