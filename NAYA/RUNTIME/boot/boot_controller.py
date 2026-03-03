from RUNTIME.environment.env_manager import EnvironmentManager
from RUNTIME.logging.logger import NayaLogger


class BootController:

    def __init__(self):
        self.env_manager = EnvironmentManager()
        self.logger = NayaLogger.setup()

    def initialize(self):

        env_info = self.env_manager.describe()

        self.logger.info("Boot initialization started")
        self.logger.info(f"Environment: {env_info}")

        return env_info
