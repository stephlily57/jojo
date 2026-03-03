"""
NAYA DASHBOARD — PROJECT ENGINE VIEW

Vue lisible de l’état des projets Naya.
Lecture uniquement, aucune action.
"""

from NAYA_DASHBOARD.connectors.project_engine_connector import ProjectEngineConnector


class ProjectEngineView:
    """
    Vue de l’état des projets.
    """

    def __init__(self, connector: ProjectEngineConnector) -> None:
        self.connector = connector

    def render(self) -> dict:
        """
        Retourne une représentation lisible de l’état des projets.
        """
        snapshot = self.connector.snapshot()

        return {
            "projects_state": snapshot.get("projects_state"),
            "last_project_event": snapshot.get("last_project_event"),
            "last_intention": snapshot.get("last_intention"),
        }
