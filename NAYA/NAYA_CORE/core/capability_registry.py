# NAYA_CORE/capability_registry.py

class CapabilityRegistry:

    def __init__(self):
        self.capabilities = {}

    def register(self, name, handler):
        self.capabilities[name] = handler

    def activate(self, name, *args, **kwargs):
        if name in self.capabilities:
            return self.capabilities[name](*args, **kwargs)
