# adaptive_evolution_core.py

from typing import Any


class AdaptiveEvolutionCore:
    """
    Gère l’évolution adaptative du système.
    Apprend des opportunités validées et ajuste l’historique stratégique.
    """

    def __init__(self) -> None:
        self.history: list[Any] = []

    def evolve(self, opportunity: dict, performance_score: float) -> None:
        """
        Enregistre une opportunité si sa performance dépasse le seuil stratégique.
        """
        if performance_score > 0.6:
            self.history.append(opportunity)


# Instance globale unique (standard Naya)
ADAPTIVE_EVOLUTION_CORE = AdaptiveEvolutionCore()
