"""
NAYA LLM INTEGRATION — OPENAI PROVIDER

Rôle :
- Exécuter une requête via OpenAI
- Retourner une réponse brute
- Ne contenir aucune logique cognitive

Ce provider ne pense pas.
Il appelle l'API.
"""

from typing import Dict, Any


class OpenAIProvider:
    """
    Provider OpenAI.
    """

    def execute(self, prompt: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Exécute un prompt via OpenAI.

        params attendus (exemples) :
        - api_key
        - model
        - temperature
        """
        if params is None:
            params = {}

        try:
            from openai import OpenAI
        except ImportError:
            return {
                "provider": "openai",
                "error": "openai package not installed",
                "output": None
            }

        api_key = params.get("api_key")
        model = params.get("model", "gpt-4o-mini")
        temperature = params.get("temperature", 0.7)

        if not api_key:
            return {
                "provider": "openai",
                "error": "No api_key provided",
                "output": None
            }

        try:
            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )

            return {
                "provider": "openai",
                "response": response,
                "raw": response.model_dump()
            }

        except Exception as exc:
            return {
                "provider": "openai",
                "error": str(exc),
                "output": None
            }
