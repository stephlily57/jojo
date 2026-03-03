from RUNTIME.environment.env_manager import EnvironmentManager
from KERNEL.activation_controller import ActivationController
import json
from datetime import datetime


def log(message: str, level: str = "INFO"):
    print(json.dumps({
        "time": datetime.utcnow().isoformat(),
        "level": level,
        "message": message
    }))


if __name__ == "__main__":

    log("Boot initialization started")

    env_manager = EnvironmentManager()
    env = env_manager.get()

    log(f"Environment: {env}")

    if not env_manager.is_production():
        raise RuntimeError("System cannot start outside PRODUCTION mode.")

    controller = ActivationController()
    controller.activate()

    print("=== NAYA SYSTEM READY — PRODUCTION LOCKED ===")
