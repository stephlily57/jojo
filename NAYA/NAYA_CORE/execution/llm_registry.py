"""
NAYA LLM INTEGRATION — LLM REGISTRY

Rôle :
- Enregistrer les providers, accelerators, external brains
- Aucun choix
- Aucun raisonnement
"""

class LLMRegistry:

    def __init__(self):
        self.providers = {}
        self.accelerators = {}
        self.external_brains = {}

    def register_provider(self, name: str, provider):
        self.providers[name] = provider

    def register_accelerator(self, name: str, accelerator):
        self.accelerators[name] = accelerator

    def register_external_brain(self, name: str, brain):
        self.external_brains[name] = brain
