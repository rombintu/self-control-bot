import telebot
from config import TOKEN
from telebot import types
from dbfunc import *
import time

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def getMessage(message):
    id_client = message.from_user.id 
    messsage_text = message.text 
    name = "@" + message.from_user.username
    commands = ['/start']
    kommands = ['Отметь меня', 'Сегодня', 'Вчера']
    keyboard = types.ReplyKeyboardMarkup()

    def print_bot(text):
        bot.send_message(id_client, text)

    if messsage_text == commands[0]:
        keyboard.row(kommands[0])
        keyboard.row(kommands[2], kommands[1])
        bot.send_message(id_client, 'Выберите действие', reply_markup=keyboard)
    elif messsage_text == kommands[0]:
        # try:
        
        print_bot(add_req(name))
        # except:
        #     print_bot("Видимо ты уже сегодня отмечался, попробуй завтра")
    elif messsage_text == kommands[1]:
        # try:
        data = select_all_today()
        buff = "Отметились сегодня:\n"
        for client in data:
            buff += f" {client[0]} || {client[1]}\n"
        print_bot(buff)
        # except:
        #     print_bot("Что то пошло не так")
    elif messsage_text == kommands[2]:
        # try:
        data = select_all_yesterday()
        buff = "Отметились вчера:\n"
        for client in data:
            buff += f" {client[0]} || {client[1]}\n"
        print_bot(buff)
        # except:
        #     print_bot("Что то пошло не так")
    else:
        keyboard.row(kommands[0])
        keyboard.row(kommands[2], kommands[1])
        bot.send_message(id_client, 'Выберите действие', reply_markup=keyboard)

if __name__ == '__main__':
    print('Bot is starting...')
    # while True:
    #     try:
    bot.polling(none_stop=True)
        # except Exception as e:
        #     print(e)
        #     time.sleep(10)