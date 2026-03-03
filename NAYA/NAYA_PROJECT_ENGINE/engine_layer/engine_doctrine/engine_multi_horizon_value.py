def horizon_value(project):
    """
    Analyse valeur court / moyen / long terme.
    """
    return {
        "short_term": project.get("short_term_value", 0),
        "mid_term": project.get("mid_term_value", 0),
        "long_term": project.get("long_term_value", 0)
    }
