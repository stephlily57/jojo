# NayaCore / premium_cost_optimization_core.py
# ------------------------------------------------------------
# Ce fichier définit l’optimisation des coûts tout en maintenant
# une perception et une crédibilité premium.
# Le premium est traité comme une perception maîtrisée,
# jamais comme une dépense excessive.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class PremiumElement:
    """
    Élément contribuant à la perception premium.
    """
    element_type: str
    perceived_value: str
    real_cost_level: str
    optimization_strategy: str
    context: Dict[str, str]


@dataclass(frozen=True)
class PremiumOptimizationPlan:
    """
    Plan d’optimisation premium à coût maîtrisé.
    """
    elements: List[PremiumElement]
    generated_at: str

    def summary(self) -> str:
        types = ", ".join(e.element_type for e in self.elements)
        return (
            f"Premium elements optimized: {len(self.elements)}\n"
            f"Elements: {types}"
        )


class PremiumCostOptimizationCore:
    """
    Cœur d’optimisation du premium à coût maîtrisé.
    Il protège la crédibilité tout en minimisant les dépenses.
    """

    def optimize(self, inputs: List[Dict[str, str]]) -> PremiumOptimizationPlan:
        """
        Génère un plan d’optimisation premium à partir d’éléments fournis.
        Aucun élément n’est ignoré.
        """
        elements: List[PremiumElement] = []

        for entry in inputs:
            element = PremiumElement(
                element_type=entry.get("type", "unspecified"),
                perceived_value=entry.get("perceived_value", "high"),
                real_cost_level=entry.get("real_cost", "low"),
                optimization_strategy=entry.get(
                    "strategy",
                    "focus_on_visible_details"
                ),
                context=entry,
            )
            elements.append(element)

        return PremiumOptimizationPlan(
            elements=elements,
            generated_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
PREMIUM_COST_OPTIMIZATION_CORE = PremiumCostOptimizationCore()
