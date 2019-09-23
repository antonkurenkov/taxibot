import telebot
from telebot import types
import time

bot = telebot.TeleBot('971158672:AAFt3SgFEtM2YEfqOixJeHoslEyleKV3iQY')
bot.delete_webhook()
@bot.message_handler(func=lambda message: True, commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('input', 'output')
    markup.row('stats', 'terms', 'chat')
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        time.sleep(2)
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'пока':
        time.sleep(2)
        bot.send_message(message.chat.id, 'Прощай!')
    elif message.text.lower() == 'input':
        time.sleep(2)
        bot.send_message(message.chat.id, 'input_method()')
    elif message.text.lower() == 'output':
        time.sleep(2)
        bot.send_message(message.chat.id, 'output_method()')
    elif message.text.lower() == 'stats':
        time.sleep(2)
        bot.send_message(message.chat.id, 'stats()')
    elif message.text.lower() == 'terms':
        time.sleep(2)
        bot.send_message(message.chat.id, 'terms()')
    elif message.text.lower() == 'chat':
        time.sleep(2)
        bot.send_message(message.chat.id, 'chat()')
    else:
        bot.send_message(message.chat.id, 'Не понимаю...')


bot.polling(none_stop=True)
