""" Just, you know, some tests
"""
import time
import logging
from unittest import TestCase

def sleep_man():
    time.sleep(2)

class ThisTest(TestCase):

    def test_foo(self):
        sleep_man()
        assert True

    def test_bar(self):
        sleep_man()
        assert True

    def test_bax(self):
        logging.warn("Baxter!!!")
        sleep_man()
        assert True
