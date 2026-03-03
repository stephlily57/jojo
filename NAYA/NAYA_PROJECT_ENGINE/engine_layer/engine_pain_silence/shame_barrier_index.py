"""
Indice de barrière de honte.
Évalue à quel point un besoin est difficile à exprimer publiquement.
Aucune exécution. Déclaratif.
"""

def compute_shame_barrier(
    social_risk: int,
    self_image_risk: int,
    exposure_fear: int
) -> dict:
    """
    Chaque paramètre est noté de 0 à 10.
    Plus l’indice est élevé, plus la douleur est tue.
    """

    index = int((social_risk + self_image_risk + exposure_fear) / 3)

    return {
        "type": "SHAME_BARRIER",
        "index": index,
        "interpretation": (
            "LOW" if index < 4 else
            "MEDIUM" if index < 7 else
            "HIGH"
        ),
        "meaning": "Plus l’indice est élevé, plus la solution doit être discrète",
        "decision_role": "NON_DECISIONNAIRE"
    }
