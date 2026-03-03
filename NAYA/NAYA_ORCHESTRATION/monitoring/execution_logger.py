from datetime import datetime

class ExecutionLogger:
    def log(self, message: str):
        print(f"[{datetime.utcnow().isoformat()}] {message}")