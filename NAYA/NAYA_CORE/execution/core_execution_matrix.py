# NayaCore / core_execution_matrix.py
# ------------------------------------------------------------
# Ce fichier définit la matrice d’exécution de NAYA.
# Il permet l’exécution totale sans priorisation.
# Les modes (parallel, hybrid, safe) sont des expressions,
# jamais des restrictions.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List
from datetime import datetime

from core_multi_horizon import MultiHorizonTarget, HorizonPlan


@dataclass(frozen=True)
class ExecutionDirective:
    """
    Directive d’exécution pour un plan donné.
    """
    horizon_type: str
    execution_mode: str
    prepared_at: str
    status: str = "READY_FOR_EXECUTION"


@dataclass(frozen=True)
class ExecutionPackage:
    """
    Ensemble des directives d’exécution pour une cible.
    """
    target_description: str
    directives: List[ExecutionDirective]
    packaged_at: str

    def summary(self) -> str:
        modes = ", ".join(d.execution_mode for d in self.directives)
        return (
            f"Target: {self.target_description}\n"
            f"Execution modes: {modes}"
        )


class ExecutionMatrix:
    """
    Matrice d’exécution de NAYA.
    Elle prépare l’exécution sans jamais la bloquer.
    """

    def prepare(self, multi_targets: List[MultiHorizonTarget]) -> List[ExecutionPackage]:
        """
        Prépare les directives d’exécution pour chaque horizon.
        Tous les horizons sont préparés sans priorisation.
        """
        packages: List[ExecutionPackage] = []

        for multi_target in multi_targets:
            directives: List[ExecutionDirective] = []

            for horizon in multi_target.horizons:
                directive = ExecutionDirective(
                    horizon_type=horizon.horizon_type,
                    execution_mode=self._select_execution_mode(horizon),
                    prepared_at=datetime.utcnow().isoformat(),
                )
                directives.append(directive)

            package = ExecutionPackage(
                target_description=multi_target.base_target.objective,
                directives=directives,
                packaged_at=datetime.utcnow().isoformat(),
            )
            packages.append(package)

        return packages

    @staticmethod
    def _select_execution_mode(horizon: HorizonPlan) -> str:
        """
        Sélectionne un mode d’exécution sans bloquer les autres.
        """
        if horizon.horizon_type == "SHORT_TERM":
            return "PARALLEL"
        if horizon.horizon_type == "MID_TERM":
            return "HYBRID"
        return "SAFE"


# Instance prête à l’usage
EXECUTION_MATRIX = ExecutionMatrix()
