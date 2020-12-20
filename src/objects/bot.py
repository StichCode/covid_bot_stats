import time

import telebot
from loguru import logger
from telebot import types
from telebot.types import ReplyKeyboardRemove

from config import CONFIG
from src.objects.covid19_statistic import CovidStats

bot = telebot.TeleBot(CONFIG.token)

text_btn = ['All info', 'Info about Russia', 'I want choose location']


def inline_mk():
    mk = types.InlineKeyboardMarkup(row_width=2)
    btn_1 = types.InlineKeyboardButton(text_btn[0], callback_data="/all")
    btn_2 = types.InlineKeyboardButton(text_btn[1], callback_data="/russia")
    btn_3 = types.InlineKeyboardButton(text_btn[2], callback_data="/loc")
    mk.add(btn_1, btn_2, btn_3)
    return mk


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    covid = CovidStats()
    # bot.send_message(message.chat.id, 'del', reply_markup=ReplyKeyboardRemove())
    logger.info("User send message {0}".format(message.chat.id))
    bot.send_message(message.chat.id, "Hello, what you want to known?", reply_markup=inline_mk())

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data == "/all":
            logger.info("User {0} requested global information".format(message.chat.id))
            bot.send_message(message.chat.id, covid.html(), parse_mode='html', reply_markup=inline_mk())
        elif call.data == "/russia":
            logger.info("User {0} requested russia information".format(message.chat.id))
            bot.send_message(message.chat.id, covid.html('location'), parse_mode='html', reply_markup=inline_mk())
        elif call.data == "/loc":
            logger.info("User {0} requested russia information".format(message.chat.id))
            bot.send_message(message.chat.id, "Not works!", reply_markup=inline_mk())


def start_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=0)
        except Exception as ex:
            logger.exception(ex)
            time.sleep(10)
