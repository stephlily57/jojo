"""
NAYA LLM INTEGRATION — LLM ROUTER

Rôle :
- Router une requête cognitive vers l'exécution
- Appliquer policies techniques
- Retourner un résultat brut
"""

class LLMRouter:

    def __init__(self, registry, policies=None):
        self.registry = registry
        self.policies = policies or []

    def route(self, provider_name: str, prompt: str, params: dict):
        provider = self.registry.providers.get(provider_name)

        if not provider:
            return {"error": "Provider not found"}

        result = provider.execute(prompt, params)

        for policy in self.policies:
            policy.evaluate(result) if hasattr(policy, "evaluate") else None

        return result
