def hunt_target(target):
    """
    Mode chasse : traque opportunités sous-exploitées.
    """
    return {
        "target": target.get("name"),
        "huntable": target.get("visibility", 0) <= 3
    }
