from bootstrap.runtime_sync.cluster_bridge import ClusterBridge
from bootstrap.registry.asset_registry import AssetRegistry


class GlobalBootstrap:

    def __init__(self):
        self.cluster = ClusterBridge()
        self.registry = AssetRegistry()

    def initialize(self):
        cluster_status = self.cluster.connect("VM_NODE", "CLOUDRUN_NODE")
        assets = self.registry.list_assets()

        return {
            "cluster": cluster_status,
            "registered_assets": len(assets),
            "status": "system_ready"
        }


if __name__ == "__main__":
    boot = GlobalBootstrap()
    print(boot.initialize())
