# NAYA_CORE/cluster_controller.py

import subprocess

class ClusterController:

    def __init__(self, group_name="naya-group", zone="europe-west9-a"):
        self.group_name = group_name
        self.zone = zone
        self.cluster_active = False

    def scale_up(self, size=3):
        subprocess.run([
            "gcloud",
            "compute",
            "instance-groups",
            "managed",
            "resize",
            self.group_name,
            f"--size={size}",
            f"--zone={self.zone}"
        ])
        self.cluster_active = True

    def scale_down(self, size=1):
        subprocess.run([
            "gcloud",
            "compute",
            "instance-groups",
            "managed",
            "resize",
            self.group_name,
            f"--size={size}",
            f"--zone={self.zone}"
        ])
        self.cluster_active = False
