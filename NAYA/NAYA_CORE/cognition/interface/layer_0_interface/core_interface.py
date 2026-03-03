"""
NAYA — LAYER 0 INTERFACE
CORE INTERFACE (VERSION FINALE)

Rôle :
- Recevoir l’intention interne de Naya Core
- Formuler une pensée brute, non interprétée
- Offrir un point d’entrée naturel vers la cognition augmentée
- Ne décider de rien
- Ne filtrer rien

Ce module ne déclenche rien.
Il exprime.
"""

from typing import Dict, Any


class CoreInterface:
    """
    Interface interne de formulation de la pensée de Naya.
    """

    def __init__(self):
        self._last_intention: str | None = None
        self._last_context: Dict[str, Any] = {}

    def express(
        self,
        intention: str,
        context: Dict[str, Any] | None = None
    ) -> Dict[str, Any]:
        """
        Exprime une intention brute issue de Naya Core.

        - aucune interprétation
        - aucune transformation
        - aucune priorisation
        """
        self._last_intention = intention
        self._last_context = context or {}

        return {
            "intention": intention,
            "context": self._last_context,
            "source": "naya_core",
            "layer": 0
        }

    # ---- Accès passifs ----

    @property
    def last_intention(self) -> str | None:
        return self._last_intention

    @property
    def last_context(self) -> Dict[str, Any]:
        return self._last_context


# =========================
# INSTANCE INTERNE UNIQUE
# =========================

core_interface = CoreInterface()
