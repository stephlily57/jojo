# event_broker_adapter.py

class EventBrokerAdapter:

    def publish(self, topic: str, payload: dict):
        print(f"[BROKER] Publishing to {topic}")

    def subscribe(self, topic: str):
        print(f"[BROKER] Subscribed to {topic}")
