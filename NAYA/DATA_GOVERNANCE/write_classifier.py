class WriteClassifier:

    GLOBAL_TYPES = {"CONSTITUTION", "LEADERSHIP", "VERSION"}
    REGIONAL_TYPES = {"BUSINESS", "CLIENT", "KPI"}
    ANALYTICAL_TYPES = {"LOG", "METRIC"}

    @classmethod
    def classify(cls, write_type):

        if write_type in cls.GLOBAL_TYPES:
            return "GLOBAL"

        if write_type in cls.REGIONAL_TYPES:
            return "REGIONAL"

        if write_type in cls.ANALYTICAL_TYPES:
            return "ANALYTICAL"

        raise ValueError("Unknown write type.")
