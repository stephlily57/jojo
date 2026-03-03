from datetime import datetime


class PerformanceMonitor:
    """
    Tracks project lifecycle metrics.
    Industrial ready for future logging extension.
    """

    def __init__(self):
        self.metrics = {}

    def register_project(self, project_name):
        self.metrics[project_name] = {
            "created_at": datetime.utcnow(),
            "last_state": None,
            "state_changes": []
        }

    def update_state(self, project_name, state):
        if project_name not in self.metrics:
            self.register_project(project_name)

        self.metrics[project_name]["last_state"] = state
        self.metrics[project_name]["state_changes"].append({
            "state": state.value if hasattr(state, "value") else str(state),
            "timestamp": datetime.utcnow()
        })

    def get_project_metrics(self, project_name):
        return self.metrics.get(project_name)

    def get_all_metrics(self):
        return self.metrics
