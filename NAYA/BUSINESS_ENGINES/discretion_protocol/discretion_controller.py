class DiscretionProtocol:

    def __init__(self):
        self.mode = "STANDARD"

    def activate_silent_mode(self):
        self.mode = "SILENT"

    def deactivate_silent_mode(self):
        self.mode = "STANDARD"

    def get_mode(self):
        return self.mode
