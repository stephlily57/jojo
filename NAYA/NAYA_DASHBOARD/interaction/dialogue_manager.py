
from NAYA_DASHBOARD.dashboard_bridge import dashboard_bridge


def handle_input(text: str) -> str:
    text = text.lower()

    if "état" in text or "status" in text:
        state = dashboard_bridge.get_current_state()
        return f"État système actuel : {state}"

    return "Commande reçue."
