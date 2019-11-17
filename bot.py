import telebot
from crawler.classes.yandex import Yandex
from crawler.classes.gett import Gett
from crawler.classes.vezet import Vezet
from crawler.classes.five_mils import Five
from crawler.classes.taxovichkof import Taxovichkof


bot = telebot.TeleBot('<INPUT YOUR TOKEN HERE>')

def switch(x):
    try:
        if x.whoami() == 'Yandex':
            return Yandex.crawl(x)
        elif x.whoami() == 'Taxovichkof':
            return Taxovichkof.crawl(x)
        elif x.whoami() == 'Gett':
            return Gett.calc(x)
        elif x.whoami() == 'Vezet':
            return Vezet.crawl(x)
        elif x.whoami() == 'Five':
            return Five.crawl(x)
    except:
        return 'switch error'

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'run':
        bot.send_message(message.chat.id, 'Считаю...')

        start = 'Санкт-Петербург Улица, Ленсовета 50к1'
        finish = 'Санкт-Петербург Улица, Гжатская, 22к4'

        result = Yandex(start,finish)
        bot.send_message(message.chat.id, 'Yandex:' + str(switch(result)))

        result = Gett(start, finish)
        bot.send_message(message.chat.id, 'Gett:' + str(switch(result)))

        result = Vezet(start, finish)
        bot.send_message(message.chat.id, 'Vezet:' + str(switch(result)))

        result = Five(start, finish)
        bot.send_message(message.chat.id, '5-000-000:' + str(switch(result)))
    else:
        try:
            start = message.text.split(';')[0]
            finish = message.text.split(';')[1]

            result = Yandex(start, finish)
            bot.send_message(message.chat.id, 'Yandex:' + str(switch(result)))

            result = Gett(start, finish)
            bot.send_message(message.chat.id, 'Gett:' + str(switch(result)))

            result = Five(start, finish)
            bot.send_message(message.chat.id, '5-000-000:' + str(switch(result)))

            result = Vezet(start, finish)
            bot.send_message(message.chat.id, 'Vezet:' + str(switch(result)))
        except:
            bot.send_message(message.chat.id, 'Сорян..')




keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('button1', 'button2')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


if __name__ == '__main__':
    bot.polling(none_stop=True)
