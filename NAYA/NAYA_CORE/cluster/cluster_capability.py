# NAYA_CORE/cluster_capability.py

class ClusterCapability:

    def __init__(self, mission_state, cluster_controller):
        self.mission_state = mission_state
        self.cluster_controller = cluster_controller

    def activate(self, mission_id):
        self.mission_state.start(mission_id)
        if not self.cluster_controller.cluster_active:
            self.cluster_controller.scale_up()

    def evaluate_shutdown(self):
        if not self.mission_state.is_any_active() and self.cluster_controller.cluster_active:
            self.cluster_controller.scale_down()
