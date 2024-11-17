import logging
import sys
# from app import app


log_level = logging.INFO
level = "DEBUG" #app.config["LOG_LEVEL"]

# Sets log level
if level == "DEBUG":
    log_level = logging.DEBUG
elif level == "INFO":
    log_level = logging.INFO
elif level == "WARNING":
    log_level = logging.WARNING
elif level == "ERROR":
    log_level = logging.ERROR
elif level == "CRITICAL":
    log_level = logging.CRITICAL
else:
    pass


logger = logging.getLogger(__name__)
logger.setLevel(log_level)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log_level)

logger_format = logging.Formatter(
    "[%(asctime)s][%(thread)d][%(levelname)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S %Z"
)
handler.setFormatter(logger_format)

logger.addHandler(handler)
