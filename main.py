from datetime import datetime, timedelta

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from lib import botan
from lib.setting import loadTelegramToken
from source.cbr import Cbr



botan_token = 'dScFHssQQEz5REsqAdnQJ3Fv-HuW29ym'  # Token got from @botaniobot

def botanTrack(message, event_name):
    uid = message.from_user
    message_dict = message.to_dict()
    botan.track(botan_token, uid, message_dict, event_name)

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
    botanTrack(update.message, 'start')

def cm_help(bot, update):
    try:
        print('command help')
        sendHelp(bot, update)
        botanTrack(update.message, 'help')
    except Exception as e:
        print(e)

def cm_yesterday(bot, update):
    sendYesteday(bot, update)
    botanTrack(update.message, 'yesterday')

def callb_text(bot, update):
    try:
        date = datetime.strptime(update.message.text, '%d %m %Y')
        print(date)
        update.message.reply_text(Cbr.getCource(date))
        botanTrack(update.message, 'for_date')
    except Exception as e:
        sendTodya(bot, update)
        botanTrack(update.message, 'text')

updater = Updater(telegramToken)

updater.dispatcher.add_handler(CommandHandler('start', cm_start))
updater.dispatcher.add_handler(CommandHandler('help', cm_help))
updater.dispatcher.add_handler(CommandHandler('yesterday', cm_yesterday))
updater.dispatcher.add_handler(MessageHandler(Filters.text, callb_text))

updater.start_polling()
updater.idle()