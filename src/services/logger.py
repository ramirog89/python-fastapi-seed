import logging
import logging.config

from src.config.logger import loggerConfig


class LoggerService:
    '''
        LoggerService class registers a custom debugger to use
        in our rest application given the loggerConfig defined
        on our config logger
    '''
    def __init__(self, path='', envvar='LOG_CFG'):
        logging.config.dictConfig(loggerConfig)
        self.logger = logging.getLogger('app_debug')

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)


loggerService = LoggerService()
