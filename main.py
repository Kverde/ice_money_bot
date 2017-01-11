from datetime import datetime, timedelta



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from source.cbr import Cbr
from source.setting import loadTelegramToken

APP_ID = 'IceMoneyBot'

telegramToken = loadTelegramToken(APP_ID)

def sendTodya(bot, update):
    update.message.reply_text(Cbr.getCource(datetime.today()))

def sendYesteday(bot, update):
    yesterday = datetime.today() - timedelta(days=1)
    update.message.reply_text(Cbr.getCource(yesterday))

def sendHelp(bot, update):
    update.message.reply_text('При отправке любого сообщения вам будет возвращены курсы валют на текущую дату.')
    update.message.reply_text('Для получения курса на опредленную дату отправьте дату в формате "дд мм гггг", например "16 8 2015"')

def cm_start(bot, update):
    sendHelp(bot, update)
    sendTodya(bot, update)

def cm_help(bot, update):
    sendHelp(bot, update)

def cm_yesterday(bot, update):
    sendYesteday(bot, update)


def callb_text(bot, update):
    try:
        date = datetime.strptime(update.message.text, '%d %m %Y')
        print(date)
        update.message.reply_text(Cbr.getCource(date))
    except Exception as e:
        sendTodya(bot, update)

updater = Updater(telegramToken)

updater.dispatcher.add_handler(CommandHandler('start', cm_start))
updater.dispatcher.add_handler(CommandHandler('help', cm_help))
updater.dispatcher.add_handler(CommandHandler('yesterday', cm_yesterday))
updater.dispatcher.add_handler(MessageHandler(Filters.text, callb_text))

updater.start_polling()
updater.idle()