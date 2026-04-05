import logging
from logtail import LogtailHandler

class LoggerService:
    def __init__(self, token, host):
        self.handler = LogtailHandler(source_token=token, host=host)
        self.logger = logging.getLogger("villa_app") # Use a fixed name
        self.logger.setLevel(logging.INFO)
        self.logger.handlers = []
        self.logger.addHandler(self.handler)

    def get_logger(self):
        return self.logger