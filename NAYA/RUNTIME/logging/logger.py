import logging
import sys


class NayaLogger:

    @staticmethod
    def setup():

        logger = logging.getLogger("NAYA")
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '{"time":"%(asctime)s","level":"%(levelname)s","message":"%(message)s"}'
        )
        handler.setFormatter(formatter)

        logger.handlers.clear()
        logger.addHandler(handler)

        return logger
