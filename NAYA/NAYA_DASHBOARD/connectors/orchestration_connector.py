"""
NAYA DASHBOARD — ORCHESTRATION CONNECTOR

Connecteur neutre vers Naya Orchestration.
Lecture d’état et transmission d’intentions uniquement.
"""


class OrchestrationConnector:
    """
    Connecteur d’observation et d’intentions vers l’Orchestration.
    """

    def __init__(self) -> None:
        self.current_state = None
        self.current_mode = None
        self.last_intention = None

    def receive_state(self, state: str, mode: str = None) -> None:
        """
        Reçoit l’état actuel de l’Orchestration.
        """
        if isinstance(state, str):
            self.current_state = state

        if mode is not None and isinstance(mode, str):
            self.current_mode = mode

    def send_intention(self, intention: str) -> None:
        """
        Transmet une intention humaine vers l’Orchestration.
        """
        if not isinstance(intention, str):
            return

        cleaned = intention.strip()
        if not cleaned:
            return

        self.last_intention = cleaned

    def snapshot(self) -> dict:
        """
        Retourne un aperçu du connecteur Orchestration.
        """
        return {
            "state": self.current_state,
            "mode": self.current_mode,
            "last_intention": self.last_intention,
        }
