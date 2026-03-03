"""
NAYA LLM INTEGRATION — N8N EXTERNAL BRAIN

Rôle :
- Appeler un workflow externe n8n
- Retourner un résultat brut
- Optionnel
"""

from typing import Dict, Any
import requests


class N8NEngine:

    def execute(self, webhook_url: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Appel simple d'un workflow n8n.
        """
        try:
            response = requests.post(webhook_url, json=payload, timeout=10)
            return {
                "status": response.status_code,
                "response": response.json()
            }
        except Exception as exc:
            return {
                "status": "error",
                "error": str(exc)
            }
