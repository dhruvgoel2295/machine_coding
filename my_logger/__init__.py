import threading
from handlers.handler import Handler
from handlers.file_handler import FileHandler
from handlers.stream_handler import StreamHandler
from logger import *
from manager import *


__all__ = [
        get_logger, set_logger, ERROR, INFO, DEBUG, NOTSET,
        FileHandler, StreamHandler, 
          ]

ERROR = 30
INFO = 20
DEBUG = 10
NOTSET = 0

_level_to_name = {
    ERROR: "ERROR"
    INFO: "INFO"
    DEBUG: "DEBUG"
    NOTSET: "NOTSET"
}

_name_to_level = {
    "ERROR": ERROR
    "INFO": INFO
    "DEBUG": DEBUG
    "NOTSET": NOTSET
}

_lock = threading.RLock()

def _acquire_lock(lock):
    if _lock:
        _lock.acquire()

def _release_lock(lock):
    if _lock:
        _lock.release()

def get_logger(self, name=""):

def set_logger(self, name=""):

