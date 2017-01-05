import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from source.cbr import Cbr
from source.setting import loadTelegramToken

APP_ID = 'IceMoneyBot'

telegramToken = loadTelegramToken(APP_ID)

def start(bot, update):
    print('start')
    update.message.reply_text('При отправке любого сообщения вам будет возвращены курсы валют на текущую дату.')
    update.message.reply_text(Cbr.getCource(datetime.datetime.today()))

def text(bot, update):
    update.message.reply_text(Cbr.getCource(datetime.datetime.today()))

updater = Updater(telegramToken)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()
updater.idle()