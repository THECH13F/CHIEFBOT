
import telebot
from telebot import types
import os, subprocess
import sys

API_TOKEN = os.environ.get("API_TOKEN", False)
bot = telebot.TeleBot(API_TOKEN)
python_path = 'python'
print("CHIEF BOT STARTED......")
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, """\
Hi This bot is made by
**CHIEF AND TEAM** 
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
            groupjoin=bot.send_message(chat_id, 'From where to satart?')
            bot.register_next_step_handler(groupjoin, joinnow)
        elif startplugin == 'Sending message':
            sending=bot.send_message(chat_id, 'please send the Promotion:-')
            bot.register_next_step_handler(sending,send)
        elif startplugin == 'update':
            # os.system('git add -A')
            
            os.system('git push')
            os.execl(sys.executable, "python3", "-m", "bot")
    except Exception as e:
        bot.reply_to(message, f'oooops \n\n {e}')
def joinnow(message):
    chat_id = message.chat.id
    Starting_group = message.text
    with open ("join.txt",'w') as f:
        f.write(Starting_group)
        f.close()
    print(F'JOINING STARTING FROM {Starting_group}')
    try:
        subprocess.run([python_path, 'joining.py'])
        bot.send_message(chat_id,"joining.... \n\n Check your saved messages")
    except Exception as e:
        bot.reply_to(message, f'\t!!!ERROR!!! \n\n {e}')
    return(Starting_group)
def send(message):
    chat_id = message.chat.id
    previous_message = message.text
    with open ("send.txt",'w') as f:
        f.write(previous_message)
        f.close()
    time=bot.send_message(chat_id, 'please write time intervel:-')
    bot.register_next_step_handler(time,intervel)
    return(previous_message)
def intervel(message):
    chat_id=message.chat.id
    stime=message.text
    with open ("intervel.txt",'w') as f:
        f.write(stime)
        f.close()
    try:
        subprocess.run([python_path, 'sending.py'])
        bot.send_message(chat_id,"Sending.... \n\n Check your saved messages")
    except Exception as e:
        bot.reply_to(message, f'\t!!!ERROR!!! \n\n {e}')
    return(stime)
# print()
if(__name__ == "__main__"):
    bot.enable_save_next_step_handlers(delay=2)
    bot.infinity_polling()
