class EntityRuntime:

    def __init__(self, state_store):
        self.state_store = state_store

    def create_entity(self, name):

        data = self.state_store.read()
        entities = data.get("entities", {})
        entities[name] = {"status": "active"}
        self.state_store.update("entities", entities)

    def adapt_entity(self, name):

        data = self.state_store.read()
        entities = data.get("entities", {})
        if name in entities:
            entities[name]["status"] = "adapted"
            self.state_store.update("entities", entities)
