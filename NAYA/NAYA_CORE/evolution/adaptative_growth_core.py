# NAYA_CORE / adaptive_growth_core.py

from typing import Dict, Any


class AdaptiveGrowthCore:
    """
    Apprentissage stratégique.
    Évolue sans régression.
    """

    def __init__(self):
        self.memory = []

    def evaluate_density(self, opportunity: Dict[str, Any]) -> float:
        value = opportunity.get("value", 0)
        urgency = opportunity.get("urgency", 0.5)
        margin = opportunity.get("margin", 0.5)

        return min(1.0, (value * 0.4 + urgency * 0.3 + margin * 0.3))

    def learn(self, opportunity: Dict[str, Any], density: float):
        if density > 0.5:
            self.memory.append(opportunity)

    def restructure(self, opportunity: Dict[str, Any]):
        opportunity["restructured"] = True
        return opportunity


ADAPTIVE_GROWTH_CORE = AdaptiveGrowthCore()
