from datetime import datetime, timedelta


from source.cbr import Cbr

about_text = '''Пожалуйста, оцените этого бота https://telegram.me/storebot?start=IceMoneyBot

Для связи с разработчиком используйте Telegram @KonstantinShpilko, сайт http://way23.ru
'''

help_text = '''При отправке любого сообщения вам будет возвращены курсы валют на текущую дату.

Для получения курса на опредленную дату отправьте дату в формате "дд мм гггг" или "дд.мм.гггг"
Примеры:
16 8 2015
15.4.2016
'''

class Domain():
    def sendStart(self, bot, update):
        self.sendHelp(bot, update)
        self.sendTodya(bot, update)

    def sendTodya(self, bot, update):
        update.message.reply_text(Cbr.getCource(datetime.today()))

    def sendYesteday(self, bot, update):
        yesterday = datetime.today() - timedelta(days=1)
        update.message.reply_text(Cbr.getCource(yesterday))

    def sendText(self, bot, update):
        try:
            try:
                date = datetime.strptime(update.message.text, '%d %m %Y')
            except:
                date = datetime.strptime(update.message.text, '%d.%m.%Y')

            update.message.reply_text(Cbr.getCource(date))
            return 'for_date'
        except Exception as e:
            self.sendTodya(bot, update)
            return 'text'

    def sendHelp(self, bot, update):
        update.message.reply_text(help_text)

    def sendAbout(self, bot, update):
        update.message.reply_text(about_text)


