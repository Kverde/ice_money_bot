import datetime
import re

from source.cbr import Cbr

about_text = '''Пожалуйста, оцените этого бота https://telegram.me/storebot?start=IceMoneyBot

Для связи с разработчиком используйте Telegram @KonstantinShpilko, сайт http://way23.ru
'''

help_text = '''При отправке любого сообщения вам будет возвращены курсы валют на текущую дату.

Для получения курса на опредленную дату отправьте дату в формате "дд мм гггг" или "дд.мм.гггг"
Примеры:
16 8 2015
15.4.2016

Для того чтобы узнать какая сумма будет при конвертации долларов или евро в рубли введите число.
'''

class Message():
    def __init__(self, cbr):
        self.cbr = cbr

    def getDesc(self, ex, date):
        header = 'Курс на {:%d.%m.%Y}'.format(date)
        res_str = '{}:\n1$ = {}\n1€ = {}'.format(header,
                                                 ex.getDollar().value,
                                                 ex.getEuro().value)
        return res_str

class MessageToday(Message):
    def getText(self):
        dt = datetime.date.today()
        ex = self.cbr.getExchangeRate(dt)
        return self.getDesc(ex, dt)

    def getEventName(self):
        return 'text'

class MessageOnDate(Message):
    def __init__(self, cbr, date):
        super().__init__(cbr)
        self.date = date

    def getText(self):
        ex = self.cbr.getExchangeRate(self.date)
        return self.getDesc(ex, self.date)

    def getEventName(self):
        return 'for_date'

templWithCost = '''

{rub1:.2f}р. = {dollar1:.2f}$
{rub1:.2f}р. = {euro1:.2f}€

{dollar2:.2f}$ = {rub2:.2f}р.
{euro2:.2f}€   = {rub3:.2f}р.'''

class MessageWithCost(Message):
    def __init__(self, cbr, val):
        super().__init__(cbr)
        self.val = val

    def getText(self):
        dt = datetime.date.today()
        ex = self.cbr.getExchangeRate(dt)

        d = ex.getDollar().value
        e = ex.getEuro().value
        r = int(self.val)

        text = self.getDesc(ex, dt)
        text += templWithCost.format(rub1 = r, dollar1 =  r / d, euro1 = r / e,
                   dollar2 = r, euro2 = r,
                   rub2 = r * d, rub3 = r * e
                   )

        return text

    def getEventName(self):
        return 'with cost'


class MessageParser():
    def __init__(self, cbr):
        self.cbr = cbr

    def parse(self, text):
        try:
            res = re.search(r'(\d{1,2})[ .]+(\d{1,2})[ .]+(\d{1,4})', text)
            if res != None:
                d = int(res.group(1))
                m = int(res.group(2))
                y = int(res.group(3))
                if y < 100:
                    y += 2000

                date = datetime.date(year=y, month=m, day=d)
                return MessageOnDate(self.cbr, date)

            res = re.search(r'\d+', text)
            if res != None:
                r = res.group(0)
                return MessageWithCost(self.cbr, r)

        except:
            None
        return MessageToday(self.cbr)



class Domain():
    def __init__(self):
        self.cbr = Cbr()
        self.messageParser = MessageParser(self.cbr);

    def sendStart(self, bot, update):
        self.sendHelp(bot, update)
        self.sendText(bot, update)

    def sendYesteday(self, bot, update):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        msg = MessageOnDate(self.cbr, yesterday)
        update.message.reply_text(msg.getText())

    def sendText(self, bot, update):
        text = update.message.text

        msg = self.messageParser.parse(text)
        update.message.reply_text(msg.getText())
        return msg.getEventName()


    def sendHelp(self, bot, update):
        update.message.reply_text(help_text)

    def sendAbout(self, bot, update):
        update.message.reply_text(about_text)


