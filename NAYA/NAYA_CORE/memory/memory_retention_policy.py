# NAYA_CORE/memory_retention_policy.py

class MemoryRetentionPolicy:

    def should_archive(self, layer, decision_context):

        if layer == "OPERATIONAL":
            return True  # rotation rapide

        if layer == "STRATEGIC":
            return False  # conserver moyen terme

        if layer == "DOCTRINE":
            return False  # conserver long terme critique
