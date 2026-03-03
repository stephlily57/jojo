class ChannelRegistry:

    def __init__(self):
        self.channels = {}

    def register_channel(self, name, has_api):
        self.channels[name] = {
            "has_api": has_api,
            "status": "ACTIVE"
        }

    def get_channel(self, name):
        return self.channels.get(name)

    def get_all_channels(self):
        return self.channels
