"""
Service Entry — SERVICE 3 : SAP ARIBA

Service exposé pour exécution stratégique
post-activation et état READY de Naya.
"""

from typing import Dict, Any
from .service_definition import NayaService


def run(context: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Point d’appel standard du service SAP Ariba.
    """
    context = context or {}

    service = NayaService()

    return {
        "execution_scope": "POST_READY",
        "priority_group": "PROJECT_FIRST_EXECUTE",
        "service_id": "SERVICE_3_SAP_ARIBA",
        "service_payload": service.deliver(),
        "pricing_base_xpf": service.base_price_xpf,
        "context": context,
    }
