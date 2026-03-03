# NayaCore / budget_leverage_core.py
# ------------------------------------------------------------
# Ce fichier définit l’usage du budget comme levier stratégique.
# Le budget n’est jamais une contrainte ni un point de départ.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class BudgetContext:
    """
    Contexte budgétaire mensuel de NAYA.
    """
    monthly_budget_eur: float
    renewable: bool
    declared_at: str


@dataclass(frozen=True)
class BudgetUsageDecision:
    """
    Décision d’utilisation du budget comme levier.
    """
    purpose: str
    amount_eur: float
    justification: str
    expected_leverage: str
    decided_at: str
    context: Dict[str, str]


class BudgetLeverageCore:
    """
    Cœur du levier budgétaire de NAYA.
    Il autorise l’usage du budget sans jamais l’imposer.
    """

    def declare_budget(self) -> BudgetContext:
        """
        Déclare le budget mensuel disponible.
        """
        return BudgetContext(
            monthly_budget_eur=200.0,
            renewable=True,
            declared_at=datetime.utcnow().isoformat(),
        )

    def decide_usage(
        self,
        purpose: str,
        amount_eur: float,
        justification: str,
        expected_leverage: str,
        context: Dict[str, str],
    ) -> BudgetUsageDecision:
        """
        Prépare une décision d’usage du budget comme levier.
        Aucune dépense n’est automatique.
        """
        return BudgetUsageDecision(
            purpose=purpose,
            amount_eur=amount_eur,
            justification=justification,
            expected_leverage=expected_leverage,
            decided_at=datetime.utcnow().isoformat(),
            context=context,
        )


# Instance prête à l’usage
BUDGET_LEVERAGE_CORE = BudgetLeverageCore()
