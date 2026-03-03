"""
Déclare le périmètre de perception autorisé.
"""

def perception_scope() -> dict:
    return {
        "scope": "FULL",
        "limits": "LEGAL_ONLY",
        "decision_role": "NON_DECISIONNAIRE"
    }
