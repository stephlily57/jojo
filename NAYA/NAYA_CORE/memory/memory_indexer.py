class MemoryIndexer:

    def index(self, memory_entries):

        index = {}

        for entry in memory_entries:
            key = entry["opportunity"].get("sector", "unknown")
            if key not in index:
                index[key] = []
            index[key].append(entry)

        return index
