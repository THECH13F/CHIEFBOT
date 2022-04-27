# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""

import telebot
from telebot import types
import os
import sys

API_TOKEN = os.environ.get("API_TOKEN", False)

bot = telebot.TeleBot(API_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, """\
Hi This bot is made by
CHEIF AND TEAM 
""")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Group Joining', 'Sending message', 'update')
    msg = bot.send_message(message.chat.id, 'choose one from them', reply_markup=markup)
    bot.register_next_step_handler(msg, plugin)


def plugin(message):
    try:
        chat_id = message.chat.id
        startplugin = message.text
        if startplugin == 'Group Joining':
            groupjoin=bot.send_message(chat_id, 'From where to satrt?')
            bot.register_next_step_handler(groupjoin, joinnow)
        elif startplugin == 'Sending message':
            sending=bot.send_message(chat_id, 'please send the Promotion:-')
            bot.register_next_step_handler(sending,send)
        elif startplugin == 'update':
            try:
                os.system('git init && git fetch origin main -f --all && pip3 install -r requirements.txt')
                bot.send_message(chat_id, 'UPDATING...........')
                os.execl(sys.executable, "python3", "-m", "__init__")
            except Exception as e:
                bot.send_message(chat_id, f'**error** \n\n{e}')
    except Exception as e:
        bot.reply_to(message, f'oooops \n\n {e}')
def joinnow(message):
    chat_id = message.chat.id
    Starting_group = message.text
    try:
        os.system('python3 joining.py')
        bot.send_message(chat_id,"joining.... \n\n Check your saved messages")
    except Exception as e:
        bot.reply_to(message, f'\t!!!ERROR!!! \n\n {e}')
def send(message):
    chat_id = message.chat.id
    previous_message = message.text
    time=bot.send_message(chat_id, 'please write time intervel:-')
    bot.register_next_step_handler(time,intervel)
def intervel(message):
    chat_id=message.chat.id
    stime=message.text
    try:
        os.system('python3 sending.py')
        bot.send_message(chat_id,"Sending.... \n\n Check your saved messages")
    except Exception as e:
        bot.reply_to(message, f'\t!!!ERROR!!! \n\n {e}')

bot.enable_save_next_step_handlers(delay=2)

bot.infinity_polling()
