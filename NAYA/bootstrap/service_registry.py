# bootstrap/service_registry.py

class ServiceRegistry:

    def __init__(self):
        self.services = {}

    def register(self, name: str, instance):
        self.services[name] = instance

    def get(self, name: str):
        return self.services.get(name)

    def all(self):
        return self.services
