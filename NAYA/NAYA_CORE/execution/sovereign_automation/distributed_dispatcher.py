# distributed_dispatcher.py

from distributed_lock import DistributedLock


class DistributedDispatcher:

    def __init__(self, job_queue):
        self.job_queue = job_queue
        self.lock = DistributedLock()

    def dispatch(self, workflow_name, context):

        job_id = context.get("job_id")

        if not job_id:
            return

        if self.lock.acquire(job_id):

            self.job_queue.push(workflow_name, context)

        else:
            print("[DISTRIBUTED] Job locked by another node")
