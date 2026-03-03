import os


class CloudRunInitializer:

    @staticmethod
    def prepare():
        port = os.getenv("PORT", "8080")
        print(f"Cloud Run Prepared on port {port}")
        return True
