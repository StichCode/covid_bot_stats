import time

import telebot
from loguru import logger
from telebot import types
from telebot.types import ReplyKeyboardRemove

from config import CONFIG
from src.objects.cache import CACHE
from src.objects.covid19_statistic import CovidStats

bot = telebot.TeleBot(CONFIG.token)
covid = CovidStats()

text_btn = ['All info', 'Info about Russia', 'I want choose location']
subs = ['subscribe', 'unsubscribe']


def inline_mk(user_id):
    mk = types.InlineKeyboardMarkup(row_width=2)
    btn_1 = types.InlineKeyboardButton(text_btn[0], callback_data="/all")
    btn_2 = types.InlineKeyboardButton(text_btn[1], callback_data="/russia")
    btn_3 = types.InlineKeyboardButton(text_btn[2], callback_data="/loc")
    text = subs[1] if CACHE.is_subs(user_id) else subs[0]
    print(text)
    btn_4 = types.InlineKeyboardButton(text, callback_data=f"/{text}")
    mk.add(btn_1, btn_2, btn_3, btn_4)
    return mk


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    if not CACHE.is_exist(message.chat.id):
        CACHE.put_user(message.chat.id, False, False)
    mk = inline_mk(message.chat.id)
    logger.info("User send message {0}".format(str(message.chat.id)))
    bot.send_message(message.chat.id, "Hello, what you want to known?", reply_markup=mk)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data == "/all":
            logger.info("User {0} requested global information".format(str(message.chat.id)))
            bot.send_message(message.chat.id, covid.html(), parse_mode='html', reply_markup=mk)
        elif call.data == "/russia":
            logger.info("User {0} requested russia information".format(str(message.chat.id)))
            bot.send_message(message.chat.id, covid.html('location'), parse_mode='html', reply_markup=mk)
        elif call.data == "/loc":
            logger.info("User {0} requested russia information".format(str(message.chat.id)))
            bot.send_message(message.chat.id, "Not works!", reply_markup=mk)
        elif call.data == '/subscribe':
            logger.info("User {0} subscribe".format(str(message.chat.id)))
            CACHE.change_subscr(message.chat.id, True)
            bot.send_message(message.chat.id, "We are glad that you are with us!",
                             reply_markup=inline_mk(message.chat.id))
        elif call.data == '/unsubscribe':
            logger.info("User {0} unsubscribe".format(str(message.chat.id)))
            CACHE.change_subscr(message.chat.id, False)
            bot.send_message(message.chat.id, "Ouuu, we will miss you!", reply_markup=inline_mk(message.chat.id))


def start_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=0)
        except Exception as ex:
            logger.exception(ex)
            time.sleep(10)
