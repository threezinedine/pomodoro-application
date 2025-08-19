import logging


logger = logging.getLogger("CONFIG")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "[%(levelname)s] - [%(name)s] - %(filename)s:%(lineno)d - %(message)s"
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
