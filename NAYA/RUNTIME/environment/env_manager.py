class EnvironmentManager:

    VERSION = "1.0.0"

    def __init__(self):
        self._config = {
            "environment": "PROD",
            "production": True,
            "cloud": True,
            "local_fallback": True,
            "leader_node": "VM",
            "distributed_mode": True,
            "business_engines_enabled": True,
            "channel_intelligence_enabled": True,
            "governance_enabled": True,
            "persistence_enabled": True
        }

    def get(self) -> dict:
        return self._config

    def is_production(self) -> bool:
        return self._config["production"]

    def is_cloud_enabled(self) -> bool:
        return self._config["cloud"]

    def version(self) -> str:
        return self.VERSION
