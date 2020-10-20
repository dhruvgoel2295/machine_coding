import my_logger
from handlers.handler import Handler
from handlers.file_handler import FileHandler
from handlers.stream_handler import StreamHandler
from log_record import LogRecord


class Logger(object):
    def __init__(self):
        self.parent = 
        self.handlers = []
        self.level = mylogger.NOTSET

    def add_handler(self, handler):
        self.handlers[handler.get_name()] = handler
        return 



    def info(self, message):
        for handler in handlers:
            if handler.get_level <= mylogger.INFO:



    def error(self, message):

    def debug(self, message):

    def set_level(self, log_level):

