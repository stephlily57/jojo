"""
NAYA LLM INTEGRATION — FALLBACK POLICY

Rôle :
- Suggérer un fallback technique
- Ne jamais imposer
- Aucune logique cognitive
"""

from typing import Dict, Any, List


class FallbackPolicy:

    def suggest(
        self,
        provider_name: str,
        available_providers: List[str]
    ) -> Dict[str, Any]:
        """
        Propose un provider alternatif si disponible.
        """
        alternatives = [
            p for p in available_providers if p != provider_name
        ]

        return {
            "fallback_suggested": bool(alternatives),
            "alternatives": alternatives
        }
