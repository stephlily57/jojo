# REAPERS/snapshot_manager.py

import os
import shutil
from typing import Dict


class SnapshotManager:
    """
    Creates and restores file snapshots.
    """

    def __init__(self, snapshot_dir: str = "REAPERS/snapshots"):
        self.snapshot_dir = snapshot_dir
        os.makedirs(self.snapshot_dir, exist_ok=True)

    def snapshot_exists(self, name: str) -> bool:
        return os.path.exists(os.path.join(self.snapshot_dir, name))

    def create_snapshot(self, name: str, filepath: str) -> None:
        if not os.path.exists(filepath):
            return

        destination = os.path.join(self.snapshot_dir, name)
        shutil.copy2(filepath, destination)

    def restore_snapshot(self, name: str, target_path: str) -> None:
        source = os.path.join(self.snapshot_dir, name)
        if os.path.exists(source):
            shutil.copy2(source, target_path)

    def ensure_snapshots(self, targets: Dict[str, str]) -> None:
        for name, path in targets.items():
            if not self.snapshot_exists(name):
                self.create_snapshot(name, path)
