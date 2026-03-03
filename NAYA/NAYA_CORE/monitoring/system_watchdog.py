class SystemWatchdog:

    def __init__(self, runtime):
        self.runtime = runtime

    def monitor(self):
        return self.runtime.health_check()
