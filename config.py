import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.ini', encoding='utf-8')

VA_NAME = config['DEFAULT']['VA_NAME']

VA_VER = "1.0"

VA_ALIAS = ('аска')

VA_IDEN = config['DEFAULT']['VA_IDEN']

VA_TBR = ('скажи', 'покажи', 'ответь', 'произнеси', 'расскажи', 'сколько', 'открой')

VA_CMD_LIST = {
    "help": ('список команд', 'команды', 'что ты умеешь', 'твои навыки', 'навыки'),
    "ctime": ('время', 'текущее время', 'сейчас времени', 'который час', 'сколько времени'),
    "joke": ('расскажи анекдот', 'рассмеши', 'шутка', 'расскажи шутку', 'пошути', 'развесели'),
    "browser": ('браузер', 'интернет'),
    "weather": ('погода', 'погоду', 'погоде'),
}