"""
NAYA DASHBOARD — CORE CONNECTOR

Connecteur neutre vers Naya Core.
Ne décide rien, ne force rien, ne bloque rien.
"""


class CoreConnector:
    """
    Connecteur de lecture et d’intentions vers Naya Core.
    """

    def __init__(self) -> None:
        self.last_intention = None
        self.last_snapshot = None

    def send_intention(self, intention: str) -> None:
        """
        Transmet une intention humaine vers Naya Core.
        """
        if not isinstance(intention, str):
            return

        cleaned = intention.strip()
        if not cleaned:
            return

        self.last_intention = cleaned

    def receive_snapshot(self, snapshot: dict) -> None:
        """
        Reçoit un état (snapshot) de Naya Core.
        """
        if not isinstance(snapshot, dict):
            return

        self.last_snapshot = snapshot

    def snapshot(self) -> dict:
        """
        Retourne un aperçu du connecteur.
        """
        return {
            "last_intention": self.last_intention,
            "last_snapshot": self.last_snapshot,
        }
