class LeadershipProtocol:
    DYNAMIC_LEADERSHIP_ENABLED = True
    LEADER_CHANGE_REQUIRES_INTEGRITY = True
    LEADER_AFFECTS_WRITE_ONLY = True

    @classmethod
    def validate(cls):
        return True
