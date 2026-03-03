
from NAYA_DASHBOARD.dashboard_bridge import dashboard_bridge

def render_monitoring_view():
    state = dashboard_bridge.get_current_state()
    return state.get("monitoring", {})
