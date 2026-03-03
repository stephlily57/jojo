
from NAYA_DASHBOARD.ui.panels.system_panel import render_system_panel
from NAYA_DASHBOARD.ui.panels.monitoring_panel import render_monitoring_panel

def render_main_layout():
    print("=== NAYA DASHBOARD ===")
    print(render_system_panel())
    print(render_monitoring_panel())
