# NAYA_CORE/economic/capital_reserve_manager.py

from typing import Dict, Any


class CapitalReserveManager:
    """
    Capital governance layer.

    Responsibilities:
    - Enforce reserve ratio
    - Validate allocation capacity
    - Split capital between reserve and operational
    """

    def __init__(self) -> None:
        self.total_capital: float = 500000.0  # Adjustable base capital
        self.reserve_ratio: float = 0.40      # 40% reserve locked

    # ---------------------------------------------------------
    # CAPITAL VALIDATION
    # ---------------------------------------------------------
    def can_allocate(self, amount: float) -> bool:
        """
        Check if requested capital can be allocated
        while respecting reserve constraint.
        """
        if amount <= 0:
            return False

        available_operational = self.get_operational_capital()

        return amount <= available_operational

    # ---------------------------------------------------------
    # CAPITAL SPLIT
    # ---------------------------------------------------------
    def allocate(self, amount: float) -> Dict[str, Any]:
        """
        Allocate capital and return structured split.
        """
        if not self.can_allocate(amount):
            return {
                "status": "REJECTED",
                "reason": "INSUFFICIENT_OPERATIONAL_CAPITAL"
            }

        reserve = self.get_reserve_capital()
        operational_remaining = self.get_operational_capital() - amount

        return {
            "status": "ALLOCATED",
            "allocated": amount,
            "reserve_locked": reserve,
            "operational_remaining": operational_remaining
        }

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------
    def get_reserve_capital(self) -> float:
        return self.total_capital * self.reserve_ratio

    def get_operational_capital(self) -> float:
        return self.total_capital * (1 - self.reserve_ratio)


# ---------------------------------------------------------
# SINGLETON INSTANCE (Production Use)
# ---------------------------------------------------------

CAPITAL_RESERVE_MANAGER = CapitalReserveManager()
