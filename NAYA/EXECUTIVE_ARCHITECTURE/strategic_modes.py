class StrategicModes:

    def __init__(self):
        self.mode = "CONSERVATIVE"

    def current_mode(self, reserve_ratio):

        if reserve_ratio >= 0.6:
            self.mode = "AGGRESSIVE"
        else:
            self.mode = "CONSERVATIVE"

        return self.mode
