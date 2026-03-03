# NayaCore / N10.py
# ------------------------------------------------------------
# Outil EXTERNE d’automatisation.
# Il n’appartient pas à NAYA.
# Il est appelé par NAYA, jamais l’inverse.
# Il est remplaçable par un outil interne futur.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime


@dataclass(frozen=True)
class ExternalAutomationRequest:
    """
    Requête envoyée par NAYA à l’outil externe.
    """
    request_type: str
    payload: Dict[str, Any]
    requested_at: str


@dataclass(frozen=True)
class ExternalAutomationResponse:
    """
    Réponse fournie par l’outil externe.
    """
    status: str
    result: Dict[str, Any]
    responded_at: str


class N10ExternalTool:
    """
    Représentation d’un outil externe type n8n.
    Aucune logique métier NAYA ne doit résider ici.
    """

    def execute(self, request: ExternalAutomationRequest) -> ExternalAutomationResponse:
        """
        Exécute une tâche externe à la demande de NAYA.
        """
        # ⚠️ Simulation volontairement neutre
        # Toute logique réelle sera externe à NAYA.
        return ExternalAutomationResponse(
            status="EXECUTED",
            result={
                "request_type": request.request_type,
                "processed": True,
                "payload_snapshot": request.payload,
            },
            responded_at=datetime.utcnow().isoformat(),
        )


# Instance externe (appelée explicitement par NAYA)
N10_TOOL = N10ExternalTool()
