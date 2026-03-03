class ZeroWasteDoctrine:

    def __init__(self):
        self.framework_archive = []

    def register_framework(self, framework_name):
        self.framework_archive.append(framework_name)

    def archive_size(self):
        return len(self.framework_archive)
