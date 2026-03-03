# NayaCore / intelligence_core.py
# ------------------------------------------------------------
# Ce fichier définit l’intelligence business transversale de NAYA.
# Il amplifie la compréhension et la combinaison,
# sans jamais imposer de décision.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class IntelligenceInsight:
    """
    Insight généré par l’intelligence de NAYA.
    """
    topic: str
    observation: str
    generated_at: str
    confidence_level: float
    context: Dict[str, str]


@dataclass(frozen=True)
class IntelligenceBundle:
    """
    Ensemble d’insights produits à partir de plusieurs sources.
    """
    insights: List[IntelligenceInsight]
    bundled_at: str

    def summary(self) -> str:
        return (
            f"Insights generated: {len(self.insights)}\n"
            f"Bundled at: {self.bundled_at}"
        )


class IntelligenceCore:
    """
    Intelligence business de NAYA.
    Combine et éclaire sans diriger.
    """

    def synthesize(self, inputs: List[Dict[str, str]]) -> IntelligenceBundle:
        """
        Transforme des entrées diverses en insights exploitables.
        Aucun input n’est ignoré.
        """
        insights: List[IntelligenceInsight] = []

        for entry in inputs:
            insight = IntelligenceInsight(
                topic=entry.get("topic", "general"),
                observation=entry.get("observation", ""),
                generated_at=datetime.utcnow().isoformat(),
                confidence_level=float(entry.get("confidence", 0.5)),
                context=entry,
            )
            insights.append(insight)

        return IntelligenceBundle(
            insights=insights,
            bundled_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
INTELLIGENCE_CORE = IntelligenceCore()
