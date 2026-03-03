# NayaCore / outils_futurs.py
# ------------------------------------------------------------
# Registre stratégique des outils externes utilisés par NAYA
# et destinés à être internalisés dans le futur.
# Ce fichier n’impose aucun calendrier ni priorité.
# ------------------------------------------------------------

from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime


@dataclass(frozen=True)
class FutureInternalTool:
    """
    Outil externe identifié comme candidat à internalisation.
    """
    tool_name: str
    current_status: str
    replacement_intent: str
    identified_at: str
    notes: Dict[str, str]


@dataclass(frozen=True)
class FutureToolsRegistry:
    """
    Registre des outils externes à internaliser plus tard.
    """
    tools: List[FutureInternalTool]
    registered_at: str

    def summary(self) -> str:
        names = ", ".join(tool.tool_name for tool in self.tools)
        return (
            f"Future internal tools identified: {len(self.tools)}\n"
            f"Tools: {names}"
        )


class FutureToolsCore:
    """
    Cœur de mémoire stratégique des outils futurs.
    Il informe sans contraindre.
    """

    def register(self, inputs: List[Dict[str, str]]) -> FutureToolsRegistry:
        """
        Enregistre des outils externes à internaliser plus tard.
        """
        tools: List[FutureInternalTool] = []

        for entry in inputs:
            tool = FutureInternalTool(
                tool_name=entry.get("name", "unspecified_tool"),
                current_status=entry.get("status", "external"),
                replacement_intent=entry.get(
                    "intent",
                    "to_be_internalized_when_relevant"
                ),
                identified_at=datetime.utcnow().isoformat(),
                notes=entry,
            )
            tools.append(tool)

        return FutureToolsRegistry(
            tools=tools,
            registered_at=datetime.utcnow().isoformat(),
        )


# Instance prête à l’usage
FUTURE_TOOLS_CORE = FutureToolsCore()
