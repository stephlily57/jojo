"""
NAYA LLM INTEGRATION — GHOST POLICY

Rôle :
- Détecter des exécutions fantômes (silence, vide, incohérence)
- Ne jamais bloquer
- Retourner un signal technique exploitable par le router
"""

from typing import Dict, Any


class GhostPolicy:

    def evaluate(self, execution_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse un résultat d'exécution LLM.
        """
        if not execution_result:
            return {
                "ghost_detected": True,
                "reason": "Empty execution result"
            }

        if execution_result.get("output") in ("", None):
            return {
                "ghost_detected": True,
                "reason": "Null or empty output"
            }

        return {
            "ghost_detected": False,
            "reason": None
        }
