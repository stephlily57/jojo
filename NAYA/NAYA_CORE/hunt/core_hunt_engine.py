# NayaCore / core_hunt_engine.py
# ------------------------------------------------------------
# Ce fichier définit la chasse business de NAYA.
# La chasse n'est pas une exploration.
# Toute détection est considérée comme exploitable par nature.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class BusinessSignal:
    """
    Signal business détecté par NAYA.
    Tout signal est considéré comme exploitable.
    """
    source: str
    description: str
    detected_at: str
    confidence_level: float
    context: Dict[str, str]


@dataclass(frozen=True)
class HuntResult:
    """
    Résultat de chasse structuré.
    """
    signals: List[BusinessSignal]
    hunted_at: str
    total_signals: int

    def summary(self) -> str:
        return (
            f"Hunt date: {self.hunted_at}\n"
            f"Signals detected: {self.total_signals}"
        )


class HuntEngine:
    """
    Moteur de chasse business.
    Il ne filtre pas, il structure.
    """

    def hunt(self, raw_inputs: List[Dict[str, str]]) -> HuntResult:
        """
        Transforme des entrées brutes en signaux exploitables.
        Aucun signal n'est ignoré.
        """
        signals: List[BusinessSignal] = []

        for entry in raw_inputs:
            signal = BusinessSignal(
                source=entry.get("source", "unknown"),
                description=entry.get("description", ""),
                detected_at=datetime.utcnow().isoformat(),
                confidence_level=float(entry.get("confidence", 0.5)),
                context=entry
            )
            signals.append(signal)

        return HuntResult(
            signals=signals,
            hunted_at=datetime.utcnow().isoformat(),
            total_signals=len(signals)
        )


# Instance prête à l’usage
HUNT_ENGINE = HuntEngine()
