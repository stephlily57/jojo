# NayaCore / zero_cost_leverage_core.py
# ------------------------------------------------------------
# Ce fichier définit le principe du zéro coût initial.
# Toute création business de NAYA doit pouvoir exister,
# être lancée et exécutée sans budget.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class FreeResource:
    """
    Ressource gratuite exploitable par NAYA.
    """
    resource_type: str
    description: str
    availability_level: str
    context: Dict[str, str]


@dataclass(frozen=True)
class ZeroCostPlan:
    """
    Plan d’exploitation sans coût.
    """
    resources: List[FreeResource]
    generated_at: str

    def summary(self) -> str:
        types = ", ".join(r.resource_type for r in self.resources)
        return (
            f"Free resources identified: {len(self.resources)}\n"
            f"Resource types: {types}"
        )


class ZeroCostLeverageCore:
    """
    Cœur du levier zéro coût.
    Il identifie et structure les ressources gratuites
    avant toute considération budgétaire.
    """

    def identify_resources(self, inputs: List[Dict[str, str]]) -> ZeroCostPlan:
        """
        Identifie des ressources gratuites exploitables.
        Aucune ressource gratuite n’est ignorée.
        """
        resources: List[FreeResource] = []

        for entry in inputs:
            resource = FreeResource(
                resource_type=entry.get("type", "unspecified"),
                description=entry.get("description", ""),
                availability_level=entry.get("availability", "available"),
                context=entry,
            )
            resources.append(resource)

        return ZeroCostPlan(
            resources=resources,
            generated_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
ZERO_COST_LEVERAGE_CORE = ZeroCostLeverageCore()
