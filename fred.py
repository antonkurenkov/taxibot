import telepot

bot = telepot.Bot('971158672:AAFt3SgFEtM2YEfqOixJeHoslEyleKV3iQY')
bot.getMe()

response = bot.getUpdates()
print(response)

#
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')
#     elif message.text.lower() == 'run':
#         bot.send_message(message.chat.id, 'Считаю...')
#     elif message.text.lower() == 'alt':
#         bot.send_message(message.chat.id, 'Не понимаю..')
#
#
# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('Привет', 'Пока')
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
#     #bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
#
# bot.polling()
