class EventBus:

    def __init__(self):
        self.events = []

    def publish(self, event_type, payload):
        event = {
            "type": event_type,
            "payload": payload
        }
        self.events.append(event)

    def get_events(self):
        return self.events
