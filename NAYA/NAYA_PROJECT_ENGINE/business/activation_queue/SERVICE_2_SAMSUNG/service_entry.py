"""
Service Entry — SERVICE 2 : SAMSUNG

Service exposé pour exécution prioritaire
après activation universelle et état READY de Naya.
"""

from typing import Dict, Any
from .service_definition import NayaService


def run(context: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Point d’appel standard du service Samsung.
    """
    context = context or {}

    service = NayaService()

    return {
        "execution_scope": "POST_READY",
        "priority_group": "PROJECT_FIRST_EXECUTE",
        "service_id": "SERVICE_2_SAMSUNG",
        "service_payload": service.deliver(),
        "pricing_base_xpf": service.base_price_xpf,
        "context": context,
    }
