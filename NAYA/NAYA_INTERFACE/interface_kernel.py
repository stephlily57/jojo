from datetime import datetime
from typing import Dict, Any

class InterfaceKernel:
    """
    Central inter-module communication layer.
    """

    def __init__(self):
        self._modules = {}
        self._boot_time = datetime.utcnow()

    def register_module(self, name: str, instance: Any):
        self._modules[name] = instance

    def get_module(self, name: str):
        return self._modules.get(name)

    def system_state(self) -> Dict[str, Any]:
        return {
            "modules_registered": list(self._modules.keys()),
            "boot_time": self._boot_time
        }
