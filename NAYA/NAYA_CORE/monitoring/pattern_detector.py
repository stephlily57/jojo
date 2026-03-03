# NAYA_CORE/pattern_detector.py

class PatternDetector:

    def detect_patterns(self, strategic_memory):

        patterns = {}

        for entry in strategic_memory:
            mission = entry.get("mission_id")
            decision = entry.get("decision")

            key = str(decision)

            if key not in patterns:
                patterns[key] = 0

            patterns[key] += 1

        return patterns
