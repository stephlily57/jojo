import inspect


def enforce_entrypoint_execution():
    """
    Prevent direct execution of internal modules.
    Must only be executed through entrypoint.
    """

    stack = inspect.stack()

    for frame in stack:
        if "entrypoint.py" in frame.filename:
            return True

    raise RuntimeError(
        "Direct execution blocked. Use NAYA_PROJECT_ENGINE.entrypoint."
    )
