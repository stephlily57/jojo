class StrategicContext:

    def __init__(self, state_store):
        self.state_store = state_store

    def snapshot(self):
        state = self.state_store.read()

        return {
            "capital": state.get("capital", 0),
            "exposure": state.get("exposure", 0),
            "dependency": state.get("dependency", 0),
            "cluster_load": state.get("cluster_load", 0)
        }
