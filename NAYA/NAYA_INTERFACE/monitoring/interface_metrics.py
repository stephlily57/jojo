class InterfaceMetrics:

    def __init__(self):
        self.request_count = 0

    def increment(self):
        self.request_count += 1