import unittest
import datetime

from cbr import Cbr

class TestCbr(unittest.TestCase):
    def test_getValuteDict(self):
        valutes = Cbr.getValuteDict(datetime.date(2017, 1, 1))

        self.assertIsInstance(valutes, dict)


