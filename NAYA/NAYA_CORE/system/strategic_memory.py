class StrategicMemory:

    def __init__(self, state_store):
        self.state_store = state_store

    def store(self, opportunity):

        if opportunity.get("value", 0) < 10000:
            return

        data = self.state_store.read()
        archive = data.get("archive", [])
        archive.append(opportunity)
        self.state_store.update("archive", archive)
