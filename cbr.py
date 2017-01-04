import datetime
import requests

# описание API
# http://www.cbr.ru/scripts/Root.asp?PrtId=SXML
# пример запроса
# http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002

def getCource(date):
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

    date_str = '{:%d/%m/%Y}'.format(date)
    params = {'date_req':date_str}


    res = requests.get(URL, params=params)
    return res


x = getCource(datetime.datetime.today())
print(x)

