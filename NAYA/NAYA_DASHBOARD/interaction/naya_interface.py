"""
NAYA DASHBOARD — NAYA INTERFACE

Point de contact unique et souverain entre le Dashboard et Naya.
Toute interaction humaine transite par ce module.
"""

from dashboard_state import DashboardState
from dashboard_permissions import DashboardPermissions
from NAYA_DASHBOARD.interface.text_channel import TextChannel
from NAYA_DASHBOARD.interface.voice_channel import VoiceChannel


class NayaInterface:
    """
    Interface souveraine de communication avec Naya.
    """

    def __init__(
        self,
        state: DashboardState,
        permissions: DashboardPermissions,
    ) -> None:
        self.state = state
        self.permissions = permissions

        self.text_channel = TextChannel()
        self.voice_channel = VoiceChannel()

    def send_text(self, message: str) -> None:
        """
        Envoie une intention texte vers Naya.
        """
        if not self.permissions.can_exchange():
            return

        self.text_channel.send(message)

    def send_voice(self, message: str) -> None:
        """
        Envoie une intention vocale vers Naya.
        """
        if not self.permissions.can_exchange():
            return

        self.voice_channel.send(message)

    def snapshot(self) -> dict:
        """
        Retourne un état lisible de l’interface.
        """
        return {
            "dashboard_started": self.state.is_started(),
            "can_exchange": self.permissions.can_exchange(),
        }
