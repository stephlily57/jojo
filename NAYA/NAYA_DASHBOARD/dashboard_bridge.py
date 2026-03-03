
from typing import Dict, Any, Callable
from NAYA_INTERFACE.bus.state_stream import state_stream


class DashboardBridge:
    def __init__(self) -> None:
        self._last_state: Dict[str, Dict[str, Any]] = {}
        self._listeners: list[Callable[[Dict[str, Dict[str, Any]]], None]] = []
        state_stream.subscribe(self._on_state_update)

    def _on_state_update(self, state: Dict[str, Dict[str, Any]]) -> None:
        self._last_state = state
        for listener in list(self._listeners):
            try:
                listener(state)
            except Exception:
                pass

    def get_current_state(self) -> Dict[str, Dict[str, Any]]:
        return self._last_state.copy()

    def subscribe(self, callback: Callable[[Dict[str, Dict[str, Any]]], None]) -> None:
        if callback not in self._listeners:
            self._listeners.append(callback)

    def unsubscribe(self, callback: Callable[[Dict[str, Dict[str, Any]]], None]) -> None:
        if callback in self._listeners:
            self._listeners.remove(callback)


dashboard_bridge = DashboardBridge()
