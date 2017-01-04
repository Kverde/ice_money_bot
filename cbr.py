import datetime
from xml.etree import ElementTree

import requests

# описание API
# http://www.cbr.ru/scripts/Root.asp?PrtId=SXML
# пример запроса
# http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002

def getCource(date):
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

    date_str = '{:%d/%m/%Y}'.format(date)
    params = {'date_req':date_str}


    response = requests.get(URL, params=params)
    xml = ElementTree.fromstring(response.text)

    res = {}
    for element in xml:
        valute_id = element.get('ID')
        valute_value = element.find('Value').text

        res[valute_id] = valute_value

    DOLLAR_ID = 'R01235'
    EURO_ID = 'R01239'

    header = 'Курс на {:%d.%m.%Y}'.format(date)
    res_str = '{}:\n1$ = {}\n1e = {}'.format(header, res[DOLLAR_ID], res[EURO_ID])
    return res_str


x = getCource(datetime.datetime.today())
print(x)

