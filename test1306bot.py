import telebot

bot = telebot.TeleBot('987669302:AAGnJdElKiBTK1Ju81pX9mtprSQ4XddT7IU')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('button1', 'button2')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

if __name__ == '__main__':
    bot.polling(none_stop=True)
