import telebot
from telebot import apihelper, types

from bot.config import Config
from bot.covid19_statistic import CovidStats


bot = telebot.TeleBot(Config.TOKEN)

apihelper.proxy = {'https': f'socks5://{Config.PROXY_USERNAME}:{Config.PROXY_PASSWORD}'
                            f'@{Config.PROXY_IP}:{Config.PROXY_PORT}'}

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
    if get_message == text_btn[0]:
        bot.send_message(message.chat.id, covid.convert_to_html(covid.get_all_stats()), parse_mode='html')
    elif get_message == text_btn[1]:
        bot.send_message(message.chat.id, covid.convert_to_html(covid.get_stats_by_location()), parse_mode='html')
    elif get_message == text_btn[2]:
        bot.send_message(message.chat.id, "Not works!")


bot.polling(none_stop=True, interval=1, timeout=0)