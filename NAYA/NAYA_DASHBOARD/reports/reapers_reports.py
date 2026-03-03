"""
NAYA DASHBOARD — REAPERS REPORTS

Rapport de sécurité lisible provenant de Reapers.
Lecture uniquement.
"""

from NAYA_DASHBOARD.connectors.reapers_connector import ReapersConnector


class ReapersReports:
    """
    Rapport dédié à l’état de sécurité Reapers.
    """

    def __init__(self, connector: ReapersConnector) -> None:
        self.connector = connector

    def generate(self) -> dict:
        """
        Génère un rapport de sécurité lisible.
        """
        snapshot = self.connector.snapshot()

        return {
            "security_state": snapshot.get("security_state"),
            "last_alert": snapshot.get("last_alert"),
            "last_report": snapshot.get("last_report"),
        }
