from NAYA_INTERFACE.bus.state_stream import state_stream

def publish_state(status: str = "idle") -> None:
    state_stream.update_state(
        "core",
        {
            "status": status,
            "active": False,
            "ready": True
        }
    )
