"""
Service Entry — SERVICE 1 : ALIBABA

Ce module expose le service Alibaba pour une exécution
post-activation, lorsque Naya est READY.

Aucune décision.
Aucune exécution automatique.
"""

from typing import Dict, Any
from .service_definition import NayaService


def run(context: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Point d’appel standard du service Alibaba.
    Appelé exclusivement par l’orchestration.
    """
    context = context or {}

    service = NayaService()

    return {
        "execution_scope": "POST_READY",
        "priority_group": "PROJECT_FIRST_EXECUTE",
        "service_id": "SERVICE_1_ALIBABA",
        "service_payload": service.deliver(),
        "pricing_base_xpf": service.base_price_xpf,
        "context": context,
    }
