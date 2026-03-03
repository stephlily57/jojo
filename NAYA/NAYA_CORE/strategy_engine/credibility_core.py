# NayaCore / credibility_core.py
# ------------------------------------------------------------
# Ce fichier définit la gestion de la crédibilité de NAYA.
# La crédibilité est traitée comme un actif vivant,
# à construire, maintenir et amplifier dans le temps.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class CredibilitySignal:
    """
    Signal contribuant à la crédibilité.
    """
    source: str
    description: str
    impact_level: float
    created_at: str
    context: Dict[str, str]


@dataclass(frozen=True)
class CredibilityState:
    """
    État actuel de la crédibilité.
    """
    signals: List[CredibilitySignal]
    evaluated_at: str

    def summary(self) -> str:
        total_impact = sum(signal.impact_level for signal in self.signals)
        return (
            f"Credibility signals: {len(self.signals)}\n"
            f"Total impact level: {total_impact:.2f}\n"
            f"Evaluated at: {self.evaluated_at}"
        )


class CredibilityCore:
    """
    Cœur de gestion de la crédibilité.
    Il observe, accumule et ajuste sans jamais brider la création.
    """

    def evaluate(self, inputs: List[Dict[str, str]]) -> CredibilityState:
        """
        Transforme des entrées diverses en signaux de crédibilité.
        Aucun signal n’est ignoré.
        """
        signals: List[CredibilitySignal] = []

        for entry in inputs:
            signal = CredibilitySignal(
                source=entry.get("source", "unspecified"),
                description=entry.get("description", ""),
                impact_level=float(entry.get("impact", 0.5)),
                created_at=datetime.utcnow().isoformat(),
                context=entry,
            )
            signals.append(signal)

        return CredibilityState(
            signals=signals,
            evaluated_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
CREDIBILITY_CORE = CredibilityCore()
