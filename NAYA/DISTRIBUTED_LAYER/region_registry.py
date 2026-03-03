class RegionRegistry:

    def __init__(self):
        self.regions = {}
        self.current_leader = None

    def register_region(self, region_name):
        self.regions[region_name] = {
            "status": "ACTIVE",
            "performance_score": 0
        }

    def set_performance_score(self, region_name, score):
        if region_name in self.regions:
            self.regions[region_name]["performance_score"] = score

    def get_regions(self):
        return self.regions

    def set_leader(self, region_name):
        self.current_leader = region_name

    def get_leader(self):
        return self.current_leader
