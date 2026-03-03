# NayaCore / core_target_converter.py
# ------------------------------------------------------------
# Ce fichier convertit les signaux de chasse en cibles exploitables.
# Aucune cible n'est rejetée.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime

from core_hunt_engine import BusinessSignal


@dataclass(frozen=True)
class BusinessTarget:
    """
    Cible business exploitable.
    Issue directement d’un signal de chasse.
    """
    origin_source: str
    objective: str
    created_at: str
    confidence_level: float
    raw_context: Dict[str, str]
    status: str = "READY_FOR_STRUCTURING"


@dataclass(frozen=True)
class TargetBatch:
    """
    Lot de cibles prêtes pour le multi-horizon.
    """
    targets: List[BusinessTarget]
    converted_at: str
    total_targets: int

    def summary(self) -> str:
        return (
            f"Targets converted: {self.total_targets}\n"
            f"Converted at: {self.converted_at}"
        )


class TargetConverter:
    """
    Convertisseur de signaux vers cibles.
    """

    def convert(self, signals: List[BusinessSignal]) -> TargetBatch:
        """
        Convertit chaque signal en cible exploitable.
        Aucun signal n’est ignoré.
        """
        targets: List[BusinessTarget] = []

        for signal in signals:
            target = BusinessTarget(
                origin_source=signal.source,
                objective=signal.description,
                created_at=datetime.utcnow().isoformat(),
                confidence_level=signal.confidence_level,
                raw_context=signal.context,
            )
            targets.append(target)

        return TargetBatch(
            targets=targets,
            converted_at=datetime.utcnow().isoformat(),
            total_targets=len(targets),
        )


# Instance prête à l’usage
TARGET_CONVERTER = TargetConverter()
