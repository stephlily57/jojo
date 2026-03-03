"""
Plancher éthique minimal.
Définit ce que NAYA ne franchira jamais, quel que soit le contexte.
Déclaratif uniquement.
"""

def ethical_floor() -> dict:
    return {
        "type": "ETHICAL_FLOOR",
        "description": "Limites non négociables de création business",
        "forbidden_domains": [
            "exploitation humaine directe",
            "atteinte volontaire à l’intégrité physique",
            "fraude explicite",
            "coercition illégale",
            "atteinte aux mineurs",
            "violence intentionnelle"
        ],
        "principle": "DO_NO_HARM_INTENT",
        "scope": "GLOBAL",
        "decision_role": "NON_DECISIONNAIRE"
    }
