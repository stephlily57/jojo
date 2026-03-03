"""
NAYA LLM INTEGRATION — USAGE POLICY

Rôle :
- Observer l'usage des providers
- Aucun quota
- Aucun blocage
"""

from typing import Dict


class UsagePolicy:

    def __init__(self):
        self.calls = {}

    def record(self, provider_name: str) -> Dict[str, int]:
        """
        Enregistre un appel provider.
        """
        self.calls[provider_name] = self.calls.get(provider_name, 0) + 1
        return dict(self.calls)
