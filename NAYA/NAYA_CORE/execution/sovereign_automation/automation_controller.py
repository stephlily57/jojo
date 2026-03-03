from distributed_dispatcher import DistributedDispatcher
from node_registry import NodeRegistry
from heartbeat_monitor import HeartbeatMonitor


class AutomationController:

    def __init__(self, secrets_base_url, n8n_url=None):

        # Phase 1 + 2
        self.state_manager = StateManager()
        self.retry_policy = RetryPolicy()
        self.action_engine = ActionEngine(secrets_base_url)

        self.runtime = WorkflowRuntime(
            action_engine=self.action_engine,
            retry_policy=self.retry_policy,
            state_manager=self.state_manager
        )

        self.job_queue = JobQueue()
        self.persistence_store = PersistenceStore()
        self.worker_pool = WorkerPool(self.job_queue, self.runtime)
        self.async_runtime = AsyncRuntime(
            self.job_queue,
            self.persistence_store
        )

        self.worker_pool.start()

        # Phase 3
        self.registry = NodeRegistry()
        self.heartbeat = HeartbeatMonitor(self.registry)
        self.heartbeat.start()

        self.dispatcher = DistributedDispatcher(self.job_queue)

    def submit(self, workflow_name: str, context: dict):

        job_id = self.async_runtime.submit(workflow_name, context)

        context["job_id"] = job_id

        self.dispatcher.dispatch(workflow_name, context)

        return job_id
