
from telebot.types import BotCommand

default_commands = [
    BotCommand("start", "начало работы с ботом"),
    BotCommand("help", "помощь"),
    BotCommand("joke", "случайная шутка"),
    BotCommand("jpy_to_rub", "конвертировать JPY в RUB"),
    BotCommand("cvt", "конвертировать выбранную валюту"),
    BotCommand("set_my_currency", "установить целевую валюту"),
]
