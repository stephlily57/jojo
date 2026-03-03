# NayaCore / core_multi_horizon.py
# ------------------------------------------------------------
# Ce fichier décline chaque cible business sur plusieurs horizons.
# Court, moyen et long terme sont générés simultanément.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List
from datetime import datetime

from core_target_converter import BusinessTarget


@dataclass(frozen=True)
class HorizonPlan:
    """
    Plan d’exploitation d’une cible sur un horizon donné.
    """
    horizon_type: str
    description: str
    created_at: str
    status: str = "PLANNED"


@dataclass(frozen=True)
class MultiHorizonTarget:
    """
    Cible déclinée sur plusieurs horizons.
    """
    base_target: BusinessTarget
    horizons: List[HorizonPlan]
    generated_at: str

    def summary(self) -> str:
        horizon_list = ", ".join(h.horizon_type for h in self.horizons)
        return (
            f"Target: {self.base_target.objective}\n"
            f"Horizons: {horizon_list}"
        )


class MultiHorizonEngine:
    """
    Génère les plans court, moyen et long terme pour chaque cible.
    """

    def generate(self, targets: List[BusinessTarget]) -> List[MultiHorizonTarget]:
        """
        Génère simultanément les trois horizons pour chaque cible.
        """
        multi_horizon_targets: List[MultiHorizonTarget] = []

        for target in targets:
            horizons = [
                HorizonPlan(
                    horizon_type="SHORT_TERM",
                    description="Immediate monetization or validation opportunity",
                    created_at=datetime.utcnow().isoformat(),
                ),
                HorizonPlan(
                    horizon_type="MID_TERM",
                    description="Structured growth and consolidation opportunity",
                    created_at=datetime.utcnow().isoformat(),
                ),
                HorizonPlan(
                    horizon_type="LONG_TERM",
                    description="Capitalization, brand or recurring value opportunity",
                    created_at=datetime.utcnow().isoformat(),
                ),
            ]

            multi_target = MultiHorizonTarget(
                base_target=target,
                horizons=horizons,
                generated_at=datetime.utcnow().isoformat(),
            )
            multi_horizon_targets.append(multi_target)

        return multi_horizon_targets


# Instance prête à l’usage
MULTI_HORIZON_ENGINE = MultiHorizonEngine()
