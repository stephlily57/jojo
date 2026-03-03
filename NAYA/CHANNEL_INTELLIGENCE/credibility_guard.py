class CredibilityGuard:

    def validate_content(self, content):

        if "elite" in content["body"].lower():
            return True

        return False
