from NAYA_INTERFACE.bus.state_stream import state_stream

def publish_state(status: str = "standby") -> None:
    state_stream.update_state(
        "orchestration",
        {
            "status": status,
            "running": False,
            "rules_loaded": True
        }
    )
