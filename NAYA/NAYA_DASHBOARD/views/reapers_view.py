"""
NAYA DASHBOARD — REAPERS VIEW

Vue lisible de l’état de sécurité Reapers.
Lecture uniquement, aucune action.
"""

from NAYA_DASHBOARD.connectors.reapers_connector import ReapersConnector


class ReapersView:
    """
    Vue de l’état Reapers (sécurité & survie).
    """

    def __init__(self, connector: ReapersConnector) -> None:
        self.connector = connector

    def render(self) -> dict:
        """
        Retourne une représentation lisible de l’état Reapers.
        """
        snapshot = self.connector.snapshot()

        return {
            "security_state": snapshot.get("security_state"),
            "last_alert": snapshot.get("last_alert"),
            "last_report": snapshot.get("last_report"),
        }
