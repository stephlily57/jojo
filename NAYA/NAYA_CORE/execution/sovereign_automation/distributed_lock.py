# distributed_lock.py

import os
import time
from pathlib import Path


class DistributedLock:

    def __init__(self, lock_dir="automation_locks"):
        self.lock_dir = Path(lock_dir)
        self.lock_dir.mkdir(exist_ok=True)

    def acquire(self, job_id: str, timeout=5):

        lock_file = self.lock_dir / f"{job_id}.lock"

        start = time.time()

        while time.time() - start < timeout:
            try:
                fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.close(fd)
                return True
            except FileExistsError:
                time.sleep(0.1)

        return False

    def release(self, job_id: str):

        lock_file = self.lock_dir / f"{job_id}.lock"
        if lock_file.exists():
            lock_file.unlink()
