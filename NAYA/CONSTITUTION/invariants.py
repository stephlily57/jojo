class SystemInvariants:
    PREMIUM_FLOOR_REQUIRED = True
    SOLVABILITY_REQUIRED = True
    CAPITALIZATION_REQUIRED = True
    DUAL_CORE_REQUIRED = True
    HUNT_MODE_PERMANENT = True

    @classmethod
    def validate(cls):
        if not cls.DUAL_CORE_REQUIRED:
            raise Exception("Dual-core invariant violated.")
        return True
