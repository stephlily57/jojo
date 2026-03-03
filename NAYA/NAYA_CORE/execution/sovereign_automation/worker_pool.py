# worker_pool.py

import threading


class WorkerPool:

    def __init__(self, job_queue, runtime, max_workers=3):
        self.job_queue = job_queue
        self.runtime = runtime
        self.max_workers = max_workers
        self.workers = []
        self._stop_flag = False

    def start(self):

        for _ in range(self.max_workers):
            t = threading.Thread(target=self._worker_loop, daemon=True)
            t.start()
            self.workers.append(t)

    def stop(self):
        self._stop_flag = True

    def _worker_loop(self):

        while not self._stop_flag:
            workflow_name, context = self.job_queue.pop()

            try:
                self.runtime.run(workflow_name, context)
            except Exception as e:
                print(f"[AUTOMATION] Job failed: {e}")
            finally:
                self.job_queue.task_done()
