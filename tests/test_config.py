import unittest
import logging

from mahamoti import config

class ConfigTest(unittest.TestCase):

    def test_debug_logger(self):
        config.DebugLogger.LEVEL = logging.ERROR
        logger = config.DebugLogger.instance()
        logger.event("pouac")
