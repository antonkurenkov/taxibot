import telebot
import crawler

bot = telebot.TeleBot('987669302:AAGnJdElKiBTK1Ju81pX9mtprSQ4XddT7IU')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'run':
        bot.send_message(message.chat.id, 'Считаю...')
        result = crawler.engine.main()
        bot.send_message(message.chat.id, 'time:' + str(result[0]))
        bot.send_message(message.chat.id, 'price:' + str(result[1]))



keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('button1', 'button2')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

if __name__ == '__main__':
    bot.polling(none_stop=True)