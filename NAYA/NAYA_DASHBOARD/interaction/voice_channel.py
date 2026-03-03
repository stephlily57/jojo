"""
NAYA DASHBOARD — VOICE CHANNEL

Canal de transmission des intentions humaines vocales.
Aucune reconnaissance, aucune synthèse, aucune décision.
"""


class VoiceChannel:
    """
    Canal vocal souverain.
    """

    def __init__(self) -> None:
        self.history = []

    def send(self, message: str) -> None:
        """
        Enregistre et transmet une intention vocale.
        """
        if not isinstance(message, str):
            return

        cleaned = message.strip()
        if not cleaned:
            return

        self.history.append(cleaned)

    def snapshot(self) -> dict:
        """
        Retourne un aperçu du canal vocal.
        """
        return {
            "voice_messages_sent": len(self.history),
            "last_voice_message": self.history[-1] if self.history else None,
        }
