import datetime
from xml.etree import ElementTree

import requests

# описание API
# http://www.cbr.ru/scripts/Root.asp?PrtId=SXML
# пример запроса
# http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002


class Currency():
    def __init__(self, id, value):
        self.id = id
        self.value = float(value.replace(',', '.'))


class ExchangeRate():
    DOLLAR_ID = 'R01235'
    EURO_ID = 'R01239'

    def __init__(self, date, values):
        self.date = date
        self.values = values

    def getDate(self):
        return self.date

    def getDollar(self):
        return Currency(ExchangeRate.DOLLAR_ID, self.values[ExchangeRate.DOLLAR_ID])

    def getEuro(self):
        return Currency(ExchangeRate.EURO_ID, self.values[ExchangeRate.EURO_ID])



class Cbr():
    def getExchangeRate(self, date):
        URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

        date_str = '{:%d/%m/%Y}'.format(date)
        params = {'date_req': date_str}

        response = requests.get(URL, params=params)
        xml = ElementTree.fromstring(response.text)

        res = {}
        for element in xml:
            valute_id = element.get('ID')
            valute_value = element.find('Value').text

            res[valute_id] = valute_value

        return ExchangeRate(date, res)






