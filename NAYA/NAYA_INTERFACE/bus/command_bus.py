class CommandBus:

    def __init__(self):
        self.handlers = {}

    def register(self, command, handler):
        self.handlers[command] = handler

    def execute(self, command, payload):
        if command not in self.handlers:
            raise ValueError("Unknown command")
        return self.handlers[command](payload)