# NAYA_CORE/doctrine/strategic_modes.py

class StrategicModes:

    CURRENT_MODE = "AUTO"
    MANUAL_OVERRIDE = None

    @classmethod
    def determine_mode(cls, density: float) -> str:

        if cls.MANUAL_OVERRIDE:
            return cls.MANUAL_OVERRIDE

        if density < 0.4:
            return "CONSERVATIVE"

        if density > 0.75:
            return "AGGRESSIVE"

        return "BALANCED"

    @classmethod
    def override(cls, mode: str):
        cls.MANUAL_OVERRIDE = mode

    @classmethod
    def reset_override(cls):
        cls.MANUAL_OVERRIDE = None
