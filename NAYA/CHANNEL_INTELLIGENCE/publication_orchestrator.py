class PublicationOrchestrator:

    def publish(self, channel_name, strategy, content):

        return {
            "channel": channel_name,
            "strategy": strategy,
            "status": "PUBLISHED",
            "content_summary": content["headline"]
        }
