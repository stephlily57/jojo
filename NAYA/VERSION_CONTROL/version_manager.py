class VersionManager:

    def __init__(self):
        self.current_version = "1.0.0"

    def increment_minor(self):
        major, minor, patch = map(int, self.current_version.split("."))
        minor += 1
        self.current_version = f"{major}.{minor}.{patch}"

    def get_version(self):
        return self.current_version
