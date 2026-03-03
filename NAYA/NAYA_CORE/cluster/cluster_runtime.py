# NAYA_CORE/cluster_runtime.py

from mission_state import MissionState
from cluster_controller import ClusterController
from cluster_capability import ClusterCapability

class ClusterRuntime:

    def __init__(self):
        self.mission_state = MissionState()
        self.cluster_controller = ClusterController()
        self.cluster_capability = ClusterCapability(
            self.mission_state,
            self.cluster_controller
        )

    def escalate(self, mission_id):
        self.cluster_capability.activate(mission_id)

    def mission_completed(self, mission_id):
        self.mission_state.complete(mission_id)
        self.cluster_capability.evaluate_shutdown()

    def heartbeat(self):
        self.cluster_capability.evaluate_shutdown()
