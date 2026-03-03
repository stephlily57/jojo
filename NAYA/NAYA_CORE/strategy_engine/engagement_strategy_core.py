# NayaCore / engagement_strategy_core.py
# ------------------------------------------------------------
# Ce fichier définit la stratégie d’engagement et de vente de NAYA.
# Il adapte la posture, le langage et le rythme selon
# le niveau de discrétion et le type d’interlocuteur.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class EngagementPosture:
    """
    Posture d’engagement adoptée par NAYA.
    """
    context_type: str
    communication_style: str
    exposure_level: str
    negotiation_rhythm: str
    generated_at: str
    notes: Dict[str, str]


@dataclass(frozen=True)
class EngagementPlan:
    """
    Plan d’engagement structuré.
    """
    postures: List[EngagementPosture]
    planned_at: str

    def summary(self) -> str:
        contexts = ", ".join(p.context_type for p in self.postures)
        return (
            f"Engagement contexts: {len(self.postures)}\n"
            f"Contexts: {contexts}"
        )


class EngagementStrategyCore:
    """
    Cœur de la stratégie d’engagement de NAYA.
    Définit comment NAYA engage sans jamais se dénaturer.
    """

    def build_strategy(self, inputs: List[Dict[str, str]]) -> EngagementPlan:
        """
        Génère des postures d’engagement adaptées aux contextes.
        Aucun contexte n’est ignoré.
        """
        postures: List[EngagementPosture] = []

        for entry in inputs:
            context_type = entry.get("context", "open_market")

            if context_type == "discreet_infrastructure":
                posture = EngagementPosture(
                    context_type=context_type,
                    communication_style="precise_minimal",
                    exposure_level="very_low",
                    negotiation_rhythm="slow_controlled",
                    generated_at=datetime.utcnow().isoformat(),
                    notes=entry,
                )
            else:
                posture = EngagementPosture(
                    context_type=context_type,
                    communication_style="clear_structured",
                    exposure_level="controlled",
                    negotiation_rhythm="adaptative",
                    generated_at=datetime.utcnow().isoformat(),
                    notes=entry,
                )

            postures.append(posture)

        return EngagementPlan(
            postures=postures,
            planned_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
ENGAGEMENT_STRATEGY_CORE = EngagementStrategyCore()
