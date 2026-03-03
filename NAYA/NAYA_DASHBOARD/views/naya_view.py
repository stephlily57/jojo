"""
NAYA DASHBOARD — NAYA VIEW

Vue lisible de l’état de Naya côté Dashboard.
Aucune action, aucune décision, lecture uniquement.
"""

from dashboard_state import DashboardState
from NAYA_DASHBOARD.interface.naya_interface import NayaInterface


class NayaView:
    """
    Vue de l’état de Naya.
    """

    def __init__(
        self,
        state: DashboardState,
        interface: NayaInterface,
    ) -> None:
        self.state = state
        self.interface = interface

    def render(self) -> dict:
        """
        Retourne une représentation lisible de l’état Naya.
        """
        return {
            "dashboard": self.state.snapshot(),
            "interface": self.interface.snapshot(),
        }
