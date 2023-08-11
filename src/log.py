import logging
import sys

LOGGER_NAME = "PHYST"
LOG = logging.getLogger(LOGGER_NAME)

class Log:
    logger = None
    stream_handler = None

    def __init__(self) -> None:
        if Log.logger is not None:
            return
        
        formatter = logging.Formatter(
            fmt="%(asctime)s.%(msecs)03d %(levelname)s "
                "%(message)s",
                datefmt="%Y-%m-%d %H:%M:%S")
        Log.stream_handler = logging.StreamHandler(sys.stdout)
        Log.stream_handler.setFormatter(formatter)
        Log.logger = logging.getLogger(LOGGER_NAME)
        Log.logger.addHandler(self.stream_handler)
        Log.logger.setLevel(logging.INFO)