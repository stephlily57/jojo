class MemoryClusterBridge:

    def sync(self, local_memory, remote_nodes):
        return {
            "synced_nodes": remote_nodes,
            "entries": len(local_memory)
        }
