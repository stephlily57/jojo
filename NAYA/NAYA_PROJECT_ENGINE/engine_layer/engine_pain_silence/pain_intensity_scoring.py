"""
Scoring de l’intensité de la douleur.
"""

def score_pain(frequency: int, impact: int, shame: int) -> int:
    return int((frequency + impact + shame) / 3)
