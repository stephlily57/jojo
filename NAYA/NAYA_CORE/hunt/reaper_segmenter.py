class ReaperSegmenter:

    def __init__(self):
        self.mission_reapers = {}

    def assign(self, mission_id, reaper_list):
        self.mission_reapers[mission_id] = reaper_list

    def get_for_mission(self, mission_id):
        return self.mission_reapers.get(mission_id, [])

    def release(self, mission_id):
        if mission_id in self.mission_reapers:
            del self.mission_reapers[mission_id]
