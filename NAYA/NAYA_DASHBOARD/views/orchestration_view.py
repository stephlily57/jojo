"""
NAYA DASHBOARD — ORCHESTRATION VIEW

Vue lisible de l’état d’orchestration.
Lecture uniquement, aucune action.
"""

from NAYA_DASHBOARD.connectors.orchestration_connector import OrchestrationConnector


class OrchestrationView:
    """
    Vue de l’état d’orchestration.
    """

    def __init__(self, connector: OrchestrationConnector) -> None:
        self.connector = connector

    def render(self) -> dict:
        """
        Retourne une représentation lisible de l’orchestration.
        """
        snapshot = self.connector.snapshot()

        return {
            "state": snapshot.get("state"),
            "mode": snapshot.get("mode"),
            "last_intention": snapshot.get("last_intention"),
        }
