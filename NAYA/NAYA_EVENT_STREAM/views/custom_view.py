
import json, os

def load_custom_views(config_path):
    views = {}
    if not os.path.exists(config_path):
        return views
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for view in data.get("views", []):
        name = view["name"]
        rules = view.get("filters", {})
        def predicate(evt, rules=rules):
            for k, vals in rules.items():
                if getattr(evt, k) not in vals:
                    return False
            return True
        views[name] = predicate
    return views
