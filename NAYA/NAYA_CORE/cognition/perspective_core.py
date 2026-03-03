# NayaCore / perspective_core.py
# ------------------------------------------------------------
# Ce fichier définit la perspective stratégique de NAYA.
# Il permet une lecture non standard du réel,
# orientée vers les zones ignorées, sous-exploitées ou invisibles.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class PerspectiveObservation:
    """
    Observation issue d’une lecture stratégique non standard.
    """
    focus_area: str
    insight: str
    generated_at: str
    novelty_level: float
    context: Dict[str, str]


@dataclass(frozen=True)
class PerspectiveMap:
    """
    Carte des perspectives générées par NAYA.
    """
    observations: List[PerspectiveObservation]
    mapped_at: str

    def summary(self) -> str:
        return (
            f"Perspectives generated: {len(self.observations)}\n"
            f"Mapped at: {self.mapped_at}"
        )


class PerspectiveCore:
    """
    Cœur de perspective de NAYA.
    Oriente la lecture sans jamais imposer de décision.
    """

    def generate(self, inputs: List[Dict[str, str]]) -> PerspectiveMap:
        """
        Génère des perspectives à partir d’entrées existantes.
        Aucune entrée n’est ignorée.
        """
        observations: List[PerspectiveObservation] = []

        for entry in inputs:
            observation = PerspectiveObservation(
                focus_area=entry.get("area", "undefined"),
                insight=entry.get("insight", ""),
                generated_at=datetime.utcnow().isoformat(),
                novelty_level=float(entry.get("novelty", 0.5)),
                context=entry,
            )
            observations.append(observation)

        return PerspectiveMap(
            observations=observations,
            mapped_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
PERSPECTIVE_CORE = PerspectiveCore()
