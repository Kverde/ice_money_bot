import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from setting import loadTelegramToken

import cbr

APP_ID = 'IceMoneyBot'

telegramToken = loadTelegramToken(APP_ID)

def start(bot, update):
    print('start')
    update.message.reply_text('При отправке любого сообщения боту вам будет возвращены курсы валют на текущую дату.')

def text(bot, update):
    update.message.reply_text(cbr.getCource(datetime.datetime.today()))

updater = Updater(telegramToken)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()
updater.idle()