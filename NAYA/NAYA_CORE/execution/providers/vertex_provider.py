"""
NAYA LLM INTEGRATION — VERTEX PROVIDER

Rôle :
- Exécuter une requête via Google Vertex AI
- Retourner une sortie brute
- Ne contenir aucune logique cognitive

Ce provider est un moteur d'exécution pur.
"""

from typing import Dict, Any


class VertexProvider:
    """
    Provider Google Vertex AI.
    """

    def execute(self, prompt: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Exécute un prompt via Vertex AI.

        params attendus (exemples) :
        - project_id
        - location
        - model_name
        """
        if params is None:
            params = {}

        try:
            import vertexai
            from vertexai.preview.generative_models import GenerativeModel
        except ImportError:
            return {
                "provider": "vertex",
                "error": "vertexai package not installed",
                "output": None
            }

        project_id = params.get("project_id")
        location = params.get("location", "us-central1")
        model_name = params.get("model_name")

        if not project_id or not model_name:
            return {
                "provider": "vertex",
                "error": "project_id or model_name missing",
                "output": None
            }

        try:
            vertexai.init(project=project_id, location=location)

            model = GenerativeModel(model_name)
            response = model.generate_content(prompt)

            return {
                "provider": "vertex",
                "response": response,
                "raw": response.text
            }

        except Exception as exc:
            return {
                "provider": "vertex",
                "error": str(exc),
                "output": None
            }
