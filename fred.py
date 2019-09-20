import telebot
from telebot import types
#from telebot import apihelper
#apihelper.proxy = {'https':'socks5://orbtl.s5.opennetwork.cc:999', 417554679: 'ybSXViq3'}

bot = telebot.TeleBot('971158672:AAFt3SgFEtM2YEfqOixJeHoslEyleKV3iQY')


@bot.message_handler(func=lambda message: True, commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('input', 'output')
    markup.row('stats', 'terms', 'chat')
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай!')
    elif message.text.lower() == 'input':
        bot.send_message(message.chat.id, 'input_method()')
    elif message.text.lower() == 'output':
        bot.send_message(message.chat.id, 'output_method()')
    elif message.text.lower() == 'stats':
        bot.send_message(message.chat.id, 'stats()')
    elif message.text.lower() == 'chat':
        bot.send_message(message.chat.id, 'chat()')
    else:
        bot.send_message(message.chat.id, 'Не понимаю..')


if __name__ == '__main__':
    bot.polling(none_stop=True)

#111