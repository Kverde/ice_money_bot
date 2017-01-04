from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from setting import loadTelegramToken

APP_ID = 'IceMoneyBot'

telegramToken = loadTelegramToken(APP_ID)

def start(bot, update):
    print('start')
    update.message.reply_text('Hello! Send me mathematical expression!')

def hello(bot, update):
    print('hello')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def text(bot, update):
    pass

updater = Updater(telegramToken)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text))

updater.start_polling()
updater.idle()