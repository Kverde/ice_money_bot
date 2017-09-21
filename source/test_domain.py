import datetime
import unittest

import source.cbr as cbr
import source.domain as domain

class TextMesageToday(unittest.TestCase):

    def test_get_text(self):
        msg = domain.MessageToday(cbr.Cbr())
        text = msg.getText()
        self.assertIsInstance(text, str)

class TextMesageOnDate(unittest.TestCase):

    def test_get_text(self):
        msg = domain.MessageOnDate(cbr.Cbr(), datetime.date.today())
        text = msg.getText()
        self.assertIsInstance(text, str)

class TextMesageWithCost(unittest.TestCase):

    def test_get_text(self):
        msg = domain.MessageWithCost(cbr.Cbr(), 30000)
        text = msg.getText()
        self.assertIsInstance(text, str)

class TestMessageParser(unittest.TestCase):
    def test_parse_today(self):
        parser = domain.MessageParser(cbr.Cbr())

        msg = parser.parse('dsf')
        self.assertIsInstance(msg, domain.MessageToday)

        msg = parser.parse('')
        self.assertIsInstance(msg, domain.MessageToday)

    def test_parse_today(self):
        parser = domain.MessageParser(cbr.Cbr())

        msg = parser.parse('434')
        self.assertIsInstance(msg, domain.MessageWithCost)

        msg = parser.parse('343f')
        self.assertIsInstance(msg, domain.MessageWithCost)


    def test_parse_on_date(self):
        parser = domain.MessageParser(cbr.Cbr())

        msg = parser.parse('22 03 2017')
        self.assertIsInstance(msg, domain.MessageOnDate)
        self.assertEqual(msg.date, datetime.date(day=22, month=3, year=2017))

        msg = parser.parse('  12    01       2015 ')
        self.assertIsInstance(msg, domain.MessageOnDate)
        self.assertEqual(msg.date, datetime.date(day=12, month=1, year=2015))

        msg = parser.parse('2.3.2017')
        self.assertIsInstance(msg, domain.MessageOnDate)
        self.assertEqual(msg.date, datetime.date(day=2, month=3, year=2017))

        msg = parser.parse('5 .  02 .2014  ')
        self.assertIsInstance(msg, domain.MessageOnDate)
        self.assertEqual(msg.date, datetime.date(day=5, month=2, year=2014))

        msg = parser.parse('5 .  5 . 16  ')
        self.assertIsInstance(msg, domain.MessageOnDate)
        self.assertEqual(msg.date, datetime.date(day=5, month=5, year=2016))

        msg = parser.parse('2.33.2017')
        self.assertIsInstance(msg, domain.MessageToday)

