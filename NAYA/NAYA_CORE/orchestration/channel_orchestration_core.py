# NayaCore / channel_orchestration_core.py
# ------------------------------------------------------------
# Ce fichier définit l’orchestration des canaux de NAYA.
# Les canaux sont choisis consciemment selon le contexte,
# la crédibilité, l’horizon et le niveau de discrétion.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class Channel:
    """
    Canal de communication ou de distribution.
    """
    name: str
    visibility_level: str
    discretion_level: str
    credibility_alignment: float
    context: Dict[str, str]


@dataclass(frozen=True)
class ChannelPlan:
    """
    Plan d’orchestration des canaux.
    """
    channels: List[Channel]
    planned_at: str

    def summary(self) -> str:
        names = ", ".join(channel.name for channel in self.channels)
        return (
            f"Channels selected: {len(self.channels)}\n"
            f"Channels: {names}"
        )


class ChannelOrchestrationCore:
    """
    Cœur d’orchestration des canaux.
    Sélectionne sans imposer, orchestre sans diffuser.
    """

    def orchestrate(self, inputs: List[Dict[str, str]]) -> ChannelPlan:
        """
        Transforme des informations contextuelles en plan de canaux.
        Aucun canal n’est ajouté par défaut.
        """
        channels: List[Channel] = []

        for entry in inputs:
            channel = Channel(
                name=entry.get("name", "unspecified"),
                visibility_level=entry.get("visibility", "controlled"),
                discretion_level=entry.get("discretion", "medium"),
                credibility_alignment=float(entry.get("credibility", 0.5)),
                context=entry,
            )
            channels.append(channel)

        return ChannelPlan(
            channels=channels,
            planned_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
CHANNEL_ORCHESTRATION_CORE = ChannelOrchestrationCore()
