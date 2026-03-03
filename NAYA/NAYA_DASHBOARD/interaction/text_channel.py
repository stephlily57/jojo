"""
NAYA DASHBOARD — TEXT CHANNEL

Canal de transmission des intentions humaines en texte.
Aucune logique métier, aucun traitement.
"""


class TextChannel:
    """
    Canal texte souverain.
    """

    def __init__(self) -> None:
        self.history = []

    def send(self, message: str) -> None:
        """
        Enregistre et transmet une intention texte.
        """
        if not isinstance(message, str):
            return

        cleaned = message.strip()
        if not cleaned:
            return

        self.history.append(cleaned)

    def snapshot(self) -> dict:
        """
        Retourne un aperçu du canal texte.
        """
        return {
            "messages_sent": len(self.history),
            "last_message": self.history[-1] if self.history else None,
        }
