class ModuleRegistry:
    def __init__(self):
        self._modules = {}

    def register(self, name: str, instance):
        self._modules[name] = instance

    def get(self, name: str):
        return self._modules.get(name)

    def all(self):
        return self._modules

    def __repr__(self):
        return f"<ModuleRegistry modules={list(self._modules.keys())}>"
