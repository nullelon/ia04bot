import configparser
import logging
from aiogram import Bot, Dispatcher, types

config = configparser.ConfigParser()
config.read("settings.ini")

bot = Bot(token=config['Bot']['token'], parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
