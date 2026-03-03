"""
NAYA DASHBOARD — ENTRY POINT

Ce fichier est le point d’entrée unique du Dashboard.
Il initialise l’environnement sans jamais forcer l’exécution de Naya.
"""

from dashboard_state import DashboardState
from dashboard_permissions import DashboardPermissions
from NAYA_DASHBOARD.interface.naya_interface import NayaInterface


class NayaDashboard:
    """
    Instance principale du Dashboard.
    """

    def __init__(self) -> None:
        self.state = DashboardState()
        self.permissions = DashboardPermissions()
        self.interface = NayaInterface(
            state=self.state,
            permissions=self.permissions,
        )

    def start(self) -> None:
        """
        Démarrage du dashboard.
        Aucun processus n’est déclenché automatiquement.
        """
        self.state.mark_started()


def run() -> None:
    """
    Fonction d’exécution explicite.
    """
    dashboard = NayaDashboard()
    dashboard.start()


if __name__ == "__main__":
    run()
