from NAYA_INTERFACE.bus.state_stream import state_stream

def publish_state(status: str = "loaded") -> None:
    state_stream.update_state(
        "project_engine",
        {
            "status": status,
            "executing": False,
            "projects_loaded": True
        }
    )
