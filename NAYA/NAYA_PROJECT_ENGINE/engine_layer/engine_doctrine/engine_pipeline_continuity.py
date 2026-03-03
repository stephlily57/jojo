def pipeline_continuity(state):
    """
    Garantit que le pipeline n’est jamais vide.
    """
    return {
        "pipeline_alive": len(state.get("active_projects", [])) > 0,
        "action": "REFILL" if not state.get("active_projects") else "CONTINUE"
    }
