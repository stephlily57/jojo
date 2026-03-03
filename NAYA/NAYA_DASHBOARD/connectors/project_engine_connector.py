"""
NAYA DASHBOARD — PROJECT ENGINE CONNECTOR

Connecteur neutre vers le Project Engine.
Observation des projets et transmission d’intentions humaines.
"""


class ProjectEngineConnector:
    """
    Connecteur de lecture et d’intentions vers le Project Engine.
    """

    def __init__(self) -> None:
        self.projects_state = None
        self.last_project_event = None
        self.last_intention = None

    def receive_projects_state(self, state: dict) -> None:
        """
        Reçoit l’état global des projets.
        """
        if isinstance(state, dict):
            self.projects_state = state

    def receive_project_event(self, event: dict) -> None:
        """
        Reçoit un événement lié à un projet.
        """
        if isinstance(event, dict):
            self.last_project_event = event

    def send_intention(self, intention: str) -> None:
        """
        Transmet une intention humaine vers le Project Engine.
        (ex: proposition de nouveau projet)
        """
        if not isinstance(intention, str):
            return

        cleaned = intention.strip()
        if not cleaned:
            return

        self.last_intention = cleaned

    def snapshot(self) -> dict:
        """
        Retourne un aperçu du connecteur Project Engine.
        """
        return {
            "projects_state": self.projects_state,
            "last_project_event": self.last_project_event,
            "last_intention": self.last_intention,
        }
