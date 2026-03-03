class RollbackController:

    def __init__(self, snapshot_manager):
        self.snapshot_manager = snapshot_manager

    def rollback(self):
        return self.snapshot_manager.get_latest_snapshot()
