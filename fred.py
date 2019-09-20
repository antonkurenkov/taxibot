import telebot
from telebot import types
import time
import cherrypy
#from telebot import apihelper
#apihelper.proxy = {'https':'socks5://orbtl.s5.opennetwork.cc:999', 417554679: 'ybSXViq3'}

WEBHOOK_HOST = '52.57.232.2'
WEBHOOK_PORT = 80
WEBHOOK_LISTEN = '52.57.232.2'

WEBHOOK_SSL_CERT = './webhook_cert.pem'
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % ('971158672:AAFt3SgFEtM2YEfqOixJeHoslEyleKV3iQY')

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

bot = telebot.TeleBot('971158672:AAFt3SgFEtM2YEfqOixJeHoslEyleKV3iQY')
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


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


cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
