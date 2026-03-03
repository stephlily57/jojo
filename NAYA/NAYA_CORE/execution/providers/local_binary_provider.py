"""
NAYA LLM INTEGRATION — LOCAL BINARY PROVIDER

Rôle :
- Exécuter un modèle LLM local (binaire / serveur / CLI)
- Retourner une sortie brute
- Ne contenir aucune logique cognitive

Ce provider n’interprète rien.
Il exécute.
"""

from typing import Dict, Any
import subprocess


class LocalBinaryProvider:
    """
    Provider d'exécution locale.
    """

    def execute(self, prompt: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Exécute un prompt via un binaire local.

        params possibles (exemples, non obligatoires) :
        - binary_path
        - args
        """
        if params is None:
            params = {}

        binary_path = params.get("binary_path")
        args = params.get("args", [])

        if not binary_path:
            return {
                "provider": "local_binary",
                "error": "No binary_path provided",
                "output": None
            }

        try:
            process = subprocess.run(
                [binary_path] + args,
                input=prompt,
                text=True,
                capture_output=True,
                shell=False
            )

            return {
                "provider": "local_binary",
                "stdout": process.stdout,
                "stderr": process.stderr,
                "returncode": process.returncode
            }

        except Exception as exc:
            return {
                "provider": "local_binary",
                "error": str(exc),
                "output": None
            }
