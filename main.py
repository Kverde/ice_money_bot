from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from lib import botan
from lib.setting import Setting
from source.domain import Domain

APP_ID = 'IceMoneyBot'

setting = Setting(APP_ID)

def botanTrack(message, event_name):
    if setting.botan_token == '':
        return

    uid = message.from_user
    message_dict = message.to_dict()
    botan.track(setting.botan_token, uid, message_dict, event_name)

domain = Domain()


def cm_start(bot, update):
    domain.sendStart(bot, update)
    botanTrack(update.message, 'start')

def cm_help(bot, update):
    domain.sendHelp(bot, update)
    botanTrack(update.message, 'help')

def cm_about(bot, update):
    domain.sendAbout(bot, update)
    botanTrack(update.message, 'about')

def cm_yesterday(bot, update):
    domain.sendYesteday(bot, update)
    botanTrack(update.message, 'yesterday')

def callb_text(bot, update):
    log_msg = domain.sendText(bot, update)
    botanTrack(update.message, log_msg)

updater = Updater(setting.telegram_token)

updater.dispatcher.add_handler(CommandHandler('start', cm_start))
updater.dispatcher.add_handler(CommandHandler('help', cm_help))
updater.dispatcher.add_handler(CommandHandler('about', cm_about))

updater.dispatcher.add_handler(CommandHandler('yesterday', cm_yesterday))

updater.dispatcher.add_handler(MessageHandler(Filters.text, callb_text))

updater.start_polling()
updater.idle()