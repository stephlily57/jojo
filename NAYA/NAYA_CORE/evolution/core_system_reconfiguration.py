class CoreSystemReconfiguration:

    def reconfigure(self, state, load_metrics):

        new_state = state.copy()

        if load_metrics.get("cpu", 0) > 0.8:
            new_state["scaling"] = "increase"

        if load_metrics.get("memory", 0) > 0.85:
            new_state["optimization"] = "memory_compact"

        return new_state
