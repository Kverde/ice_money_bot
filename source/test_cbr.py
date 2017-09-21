import datetime
import unittest

import source.cbr as cbr


class TestCbr(unittest.TestCase):
    def test_getExchangeRate(self):
        valutes = cbr.Cbr().getExchangeRate(datetime.date(2017, 1, 1))

        self.assertIsInstance(valutes, cbr.ExchangeRate)


class TestExchangeRate(unittest.TestCase):
    def test_getDate(self):
        er = cbr.Cbr().getExchangeRate(datetime.date(2017, 1, 1))
        self.assertIsInstance(er.getDate(), datetime.date)

    def test_getDollar(self):
        er = cbr.Cbr().getExchangeRate(datetime.date(2017, 1, 1))
        self.assertIsInstance(er.getDollar(), cbr.Currency)

    def test_getEuro(self):
        er = cbr.Cbr().getExchangeRate(datetime.date(2017, 1, 1))
        self.assertIsInstance(er.getEuro(), cbr.Currency)

class TestCurrency(unittest.TestCase):
    def test_id(self):
        er = cbr.Cbr().getExchangeRate(datetime.date(2017, 1, 1))
        cur = er.getDollar()
        self.assertIsInstance(cur.id, str)

    def test_value(self):
        er = cbr.Cbr().getExchangeRate(datetime.date(2017, 1, 1))
        cur = er.getDollar()
        self.assertIsInstance(cur.value, float)