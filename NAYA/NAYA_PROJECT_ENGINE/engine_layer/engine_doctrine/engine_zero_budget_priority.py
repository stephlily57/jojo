def zero_budget_priority(project):
    """
    Priorité absolue si zéro budget et fort levier.
    """
    return project.get("budget", 1) == 0 and project.get("leverage", 0) >= 7
