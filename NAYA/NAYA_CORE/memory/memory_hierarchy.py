# NAYA_CORE/memory_hierarchy.py

class MemoryHierarchy:

    def __init__(self, distributed_memory):
        self.memory = distributed_memory

    def store_operational(self, key, value):
        self.memory.append_to_stream("memory_operational", {
            "key": key,
            "value": str(value)
        })

    def store_strategic(self, key, value):
        self.memory.append_to_stream("memory_strategic", {
            "key": key,
            "value": str(value)
        })

    def store_doctrine(self, key, value):
        self.memory.append_to_stream("memory_doctrine", {
            "key": key,
            "value": str(value)
        })
