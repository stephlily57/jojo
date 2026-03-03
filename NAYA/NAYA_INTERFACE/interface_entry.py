# NAYA_INTERFACE/interface_entry.py

from typing import Dict, Any

from NAYA_CORE.interface_bridge import CoreInterfaceBridge
from NAYA_ORCHESTRATION.interface_bridge import OrchestrationInterfaceBridge
from NAYA_PROJECT_ENGINE.interface_bridge import ProjectEngineInterfaceBridge
from REAPERS.interface_bridge import ReapersInterfaceBridge


class NayaInterface:
    def __init__(self) -> None:
        self.bridges = {
            "core": CoreInterfaceBridge(),
            "orchestration": OrchestrationInterfaceBridge(),
            "project_engine": ProjectEngineInterfaceBridge(),
            "reapers": ReapersInterfaceBridge(),
        }

    def system_status(self) -> Dict[str, Any]:
        return {
            name: bridge.status()
            for name, bridge in self.bridges.items()
        }

    def system_capabilities(self) -> Dict[str, Any]:
        return {
            name: bridge.capabilities()
            for name, bridge in self.bridges.items()
        }

    def send_command(
        self,
        target: str,
        command: str,
        payload: Dict[str, Any] | None = None
    ) -> Dict[str, Any]:

        if target not in self.bridges:
            return {
                "error": "unknown_target",
                "target": target
            }

        return self.bridges[target].handle_command(command, payload)


# Activation locale simple (test)
if __name__ == "__main__":
    interface = NayaInterface()

    print("=== STATUS ===")
    print(interface.system_status())

    print("\n=== CAPABILITIES ===")
    print(interface.system_capabilities())

    print("\n=== TEST COMMAND ===")
    print(interface.send_command("reapers", "health_check"))
