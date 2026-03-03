class SnapshotManager:

    def __init__(self):
        self.snapshots = []

    def create_snapshot(self, state):
        self.snapshots.append(state.copy())

    def get_latest_snapshot(self):
        if not self.snapshots:
            return None
        return self.snapshots[-1]
