# async_runtime.py

import uuid


class AsyncRuntime:

    def __init__(self, job_queue, persistence_store):
        self.job_queue = job_queue
        self.persistence_store = persistence_store

    def submit(self, workflow_name: str, context: dict):

        job_id = str(uuid.uuid4())

        self.persistence_store.update_job(job_id, "queued")

        context["job_id"] = job_id

        self.job_queue.push(workflow_name, context)

        return job_id
