"""
NAYA DASHBOARD — REAPERS CONNECTOR

Connecteur de supervision vers Reapers.
Aucune action de contrôle n’est possible ici.
"""


class ReapersConnector:
    """
    Connecteur de lecture et d’intentions vers Reapers.
    """

    def __init__(self) -> None:
        self.security_state = None
        self.last_report = None
        self.last_alert = None
        self.last_intention = None

    def receive_security_state(self, state: str) -> None:
        """
        Reçoit l’état de sécurité global.
        """
        if isinstance(state, str):
            self.security_state = state

    def receive_report(self, report: dict) -> None:
        """
        Reçoit un rapport synthétique de Reapers.
        """
        if isinstance(report, dict):
            self.last_report = report

    def receive_alert(self, alert: str) -> None:
        """
        Reçoit une alerte (déjà traitée ou en cours).
        """
        if isinstance(alert, str):
            self.last_alert = alert

    def send_intention(self, intention: str) -> None:
        """
        Transmet une intention humaine vers Reapers.
        (Jamais une commande)
        """
        if not isinstance(intention, str):
            return

        cleaned = intention.strip()
        if not cleaned:
            return

        self.last_intention = cleaned

    def snapshot(self) -> dict:
        """
        Retourne un aperçu du connecteur Reapers.
        """
        return {
            "security_state": self.security_state,
            "last_report": self.last_report,
            "last_alert": self.last_alert,
            "last_intention": self.last_intention,
        }
