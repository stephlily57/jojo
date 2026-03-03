
def system_view(event):
    return event.source == "SYSTEM" or event.level in ("ERROR", "CRITICAL")
