import telebot
from telebot import types

bot = telebot.TeleBot('5587461965:AAEbygZIyquIamS4q8Z7OK5sqyBgLsEiZSs')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "и тебе привет!", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('smth.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "я тебя не понимаю", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, какое крутое фото!')

@bot.message_handler(command=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardMarkup("Посетить веб сайт", url = "https://www.youtube.com/watch?v=Omy0dszV_BA&t=2626s&ab_channel=Aleron%D0%9C%D0%B8%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%BD"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

@bot.message_handler(command=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

bot.polling(none_stop=True)

