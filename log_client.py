import logging
from logging.handlers import TimedRotatingFileHandler


# disable stderr logging (happens when the remote server is down)
logging.raiseExceptions = False
logger = logging.getLogger("localhost")
logger.setLevel(logging.DEBUG)
logger.propagate = False
logger.handlers = []
handler = TimedRotatingFileHandler(filename='log_file.log', when='midnight', backupCount=5)

handler.suffix = "%Y-%m-%d"
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


http_handler = logging.handlers.HTTPHandler('127.0.0.1:8001', '/', method='POST')
logger.addHandler(http_handler)

logger.info("hello zsolti")
