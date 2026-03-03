class CoreClusterBridge:

    def __init__(self):
        self.nodes = []

    def register_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes.append(node_id)

    def broadcast(self, payload):
        # prêt pour extension future (Redis, Kafka, gRPC, etc.)
        return {
            "nodes": self.nodes,
            "payload": payload
        }

    def health_check(self):
        return {"cluster_nodes": len(self.nodes)}
