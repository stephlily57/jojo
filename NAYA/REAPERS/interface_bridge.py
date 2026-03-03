from NAYA_INTERFACE.bus.state_stream import state_stream

def publish_state(status: str = "disconnected") -> None:
    state_stream.update_state(
        "reapers",
        {
            "status": status,
            "connected": False,
            "watching": False
        }
    )
