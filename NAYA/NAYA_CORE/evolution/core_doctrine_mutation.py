class CoreDoctrineMutation:

    def __init__(self):
        self.history = []

    def mutate(self, doctrine_state, performance_metrics):
        new_state = doctrine_state.copy()

        if performance_metrics.get("efficiency", 0) > 0.8:
            new_state["aggressiveness"] = new_state.get("aggressiveness", 1) * 1.05

        self.history.append({
            "previous": doctrine_state,
            "new": new_state,
            "metrics": performance_metrics
        })

        return new_state

    def get_history(self):
        return self.history[-10:]
