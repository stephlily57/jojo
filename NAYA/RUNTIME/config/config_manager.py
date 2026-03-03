import os


class ConfigManager:

    DEFAULT_ENV = "DEV"

    @classmethod
    def get_environment(cls):
        return os.getenv("NAYA_ENV", cls.DEFAULT_ENV)

    @classmethod
    def is_production(cls):
        return cls.get_environment() == "PROD"

    @classmethod
    def is_cloud(cls):
        return cls.get_environment() == "CLOUD"

    @classmethod
    def get_setting(cls, key, default=None):
        return os.getenv(key, default)
