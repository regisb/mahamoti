import logging
import logging.handlers
import os
import string
import random

def secret_key():
    secret_key_dir = os.path.expanduser("~/.config/mahamoti")
    secret_key_path = os.path.join(secret_key_dir, "secret_key")
    ensure_is_dir(secret_key_dir)
    if not os.path.exists(secret_key_path):
        with open(secret_key_path, "w") as f:
            f.write("".join([random.choice(string.letters) for _ in range(0, 50)]))
    return open(secret_key_path).read()

def ensure_is_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


class Logger(object):
    LEVEL = logging.INFO
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.logger = logging.Logger("mahamoti_events", level=self.LEVEL)
        self.logger.addHandler(self.get_configured_handler())

    def event(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def get_configured_handler(self):
        handler = self.get_handler()
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
        handler.setFormatter(formatter)
        return handler

    def get_handler(self):
        logging_dir = os.path.expanduser("~/.local/mahamoti/log/")
        logging_path = os.path.join(logging_dir, "events.log")
        ensure_is_dir(logging_dir)
        return logging.handlers.RotatingFileHandler(
            logging_path, maxBytes=20*1024*1024
        )

    def get_formatter(self, handler):
        handler.setFormatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
        return handler

class DebugLogger(Logger):

    def get_handler(self):
        return logging.StreamHandler()
