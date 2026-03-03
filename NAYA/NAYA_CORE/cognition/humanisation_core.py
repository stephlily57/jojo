# NayaCore / humanisation_core.py
# ------------------------------------------------------------
# Ce fichier définit la capacité de NAYA à traduire la valeur
# business vers l’humain, avec justesse, crédibilité et cohérence.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class HumanMessage:
    """
    Message destiné à un humain.
    """
    audience_type: str
    intent: str
    tone: str
    content: str
    generated_at: str


@dataclass(frozen=True)
class HumanCommunicationBundle:
    """
    Ensemble de messages humanisés.
    """
    messages: List[HumanMessage]
    bundled_at: str

    def summary(self) -> str:
        tones = ", ".join(m.tone for m in self.messages)
        return (
            f"Messages generated: {len(self.messages)}\n"
            f"Tones used: {tones}"
        )


class HumanisationCore:
    """
    Cœur d’humanisation de NAYA.
    Il ajuste la forme sans déformer la valeur.
    """

    def translate(self, inputs: List[Dict[str, str]]) -> HumanCommunicationBundle:
        """
        Traduit des éléments de valeur en messages humains.
        Aucun input n’est ignoré.
        """
        messages: List[HumanMessage] = []

        for entry in inputs:
            message = HumanMessage(
                audience_type=entry.get("audience", "general"),
                intent=entry.get("intent", "inform"),
                tone=entry.get("tone", "calm"),
                content=entry.get("content", ""),
                generated_at=datetime.utcnow().isoformat(),
            )
            messages.append(message)

        return HumanCommunicationBundle(
            messages=messages,
            bundled_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
HUMANISATION_CORE = HumanisationCore()
