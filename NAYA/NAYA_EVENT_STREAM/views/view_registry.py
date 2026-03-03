
class ViewRegistry:
    def __init__(self):
        self.views = {}

    def register(self, name, predicate):
        self.views[name] = predicate

    def match(self, view_name, event):
        if view_name not in self.views:
            return False
        return self.views[view_name](event)
