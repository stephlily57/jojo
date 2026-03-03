"""
NAYA — CASH DOCTRINE
Statut : déclaratif
Nature : stratégique
Effet : orientation (non contraignante)
"""

CASH_DOCTRINE = {
    "principes": {
        "cash_reel": {
            "definition": "Toute création doit répondre à une douleur réelle, actuelle et solvable.",
            "interpretation": "Le cash n'est jamais hypothétique, il est lié à un besoin existant.",
        },
        "cash_rapide": {
            "definition": "Toute création générant un revenu en 24h, 48h ou 72h maximum.",
            "plafond_absolu_heures": 72,
            "note": "Au-delà de 72h, la création sort automatiquement du champ 'rapide'."
        }
    },
    "temporalite": {
        "rapide": {
            "max_heures": 72,
            "nature": "urgence, douleur aiguë, décision immédiate"
        },
        "moyen_terme": {
            "min_heures": 73,
            "max_jours": 90,
            "nature": "structuration, montée en gamme, continuité"
        },
        "long_terme": {
            "min_jours": 91,
            "nature": "actifs lourds, projets stratégiques, maturité 95%"
        }
    },
    "regles": {
        "aucune_confusion": True,
        "aucune_auto_illusion": True,
        "reclassification_automatique": True
    }
}
