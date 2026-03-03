def normalize_ambition(project):
    """
    Évite la sur-ambition non alignée avec les ressources.
    """
    ambition = project.get("ambition", 5)
    resources = project.get("resources", 5)
    return min(ambition, resources)
