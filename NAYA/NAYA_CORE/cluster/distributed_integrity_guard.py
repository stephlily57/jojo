class DistributedIntegrityGuard:

    def __init__(self, cluster_nodes):
        self.cluster_nodes = cluster_nodes

    def verify_cluster_integrity(self):
        results = [node.integrity_check() for node in self.cluster_nodes]
        return all(results)
