import os
import sqlite3
from RUNTIME.config.config_manager import ConfigManager


class DatabaseManager:

    def __init__(self):
        self.env = ConfigManager.get_environment()
        self.connection = None

    def connect(self):

        if self.env == "DEV":
            self.connection = sqlite3.connect("naya_dev.db")
        else:
            # Placeholder PostgreSQL (Cloud SQL ready)
            raise NotImplementedError("PostgreSQL not configured yet")

        return self.connection

    def get_connection(self):
        if not self.connection:
            return self.connect()
        return self.connection
