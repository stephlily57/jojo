# job_queue.py

import queue
import threading


class JobQueue:

    def __init__(self):
        self._queue = queue.Queue()
        self._lock = threading.Lock()

    def push(self, workflow_name: str, context: dict):
        self._queue.put((workflow_name, context))

    def pop(self):
        return self._queue.get()

    def task_done(self):
        self._queue.task_done()

    def size(self):
        return self._queue.qsize()
