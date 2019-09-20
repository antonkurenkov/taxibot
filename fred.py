import telebot
from telebot import types
#from telebot import apihelper
#apihelper.proxy = {'https':'socks5://orbtl.s5.opennetwork.cc:999', 417554679: 'ybSXViq3'}

bot = telebot.TeleBot('971158672:AAFt3SgFEtM2YEfqOixJeHoslEyleKV3iQY')


@bot.message_handler(func=lambda message: True, commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('a', 'v')
    markup.row('c', 'd', 'e')
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'run':
        bot.send_message(message.chat.id, 'Считаю...')
    else:
        bot.send_message(message.chat.id, 'Не понимаю..')


bot.polling()
