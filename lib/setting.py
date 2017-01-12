import configparser
import os

def loadTelegramToken(appId):
    token = os.getenv('TELEGRAM_TOKEN')
    if not token is None:
        return token

    setting_path = os.getenv('ice_setting')
    if setting_path is None:
        raise Exception('System var ice_setting not found')

    settingFileName = os.path.join(setting_path, appId, 'setting.ini')

    if not os.path.exists(settingFileName):
        raise Exception('Setting file {} not found'.format(settingFileName))

    config = configparser.ConfigParser()
    config.read(settingFileName)

    return config['main']['telegram_token']