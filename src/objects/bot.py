import time

import telebot
from loguru import logger
from telebot import types

from config import CONFIG
from src.objects.covid19_statistic import CovidStats

bot = telebot.TeleBot(CONFIG.token)

text_btn = ['All info', 'Info about Russia', 'I want choose location']


def default_mk():
    mk = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_1 = types.KeyboardButton(text_btn[0])
    btn_2 = types.KeyboardButton(text_btn[1])
    btn_3 = types.KeyboardButton(text_btn[2])
    mk.add(btn_1, btn_2, btn_3)
    return mk


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello, what you want to known?", reply_markup=default_mk())


@bot.message_handler(content_types=['text'])
def info_covid19(message):
    covid = CovidStats()
    get_message = message.text
    logger.info("User: {}".format(message.chat.id))
    if get_message == text_btn[0]:
        bot.send_message(message.chat.id, covid.html(), parse_mode='html')
    elif get_message == text_btn[1]:
        bot.send_message(message.chat.id, covid.html('location'), parse_mode='html')
    elif get_message == text_btn[2]:
        bot.send_message(message.chat.id, "Not works!")


def start_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=0)
        except Exception as ex:
            logger.exception(ex)
            time.sleep(10)
