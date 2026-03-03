
from NAYA_DASHBOARD.dashboard_bridge import dashboard_bridge

def render_system_view() -> dict:
    """Retourne une vue système synthétique et lisible."""
    state = dashboard_bridge.get_current_state()

    return {
        "interface": state.get("interface"),
        "core": state.get("core"),
        "orchestration": state.get("orchestration"),
        "project_engine": state.get("project_engine"),
        "reapers": state.get("reapers"),
    }
