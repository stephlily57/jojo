from typing import Dict, Any

class InterfaceRouter:
    """
    Routes commands between modules.
    """

    def dispatch(self, target, method: str, payload: Dict[str, Any]):
        if not hasattr(target, method):
            return {"status": "error", "reason": "method_not_found"}

        handler = getattr(target, method)
        return handler(payload)
