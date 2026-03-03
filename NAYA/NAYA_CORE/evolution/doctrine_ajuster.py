# NAYA_CORE/doctrine_adjuster.py

class DoctrineAdjuster:

    def adjust(self, doctrine_engine, detected_patterns):

        for decision, frequency in detected_patterns.items():

            if frequency > 5:
                doctrine_engine.reinforce(decision)

            if frequency > 10:
                doctrine_engine.prioritize(decision)
