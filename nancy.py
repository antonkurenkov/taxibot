from flask import Flask, request
import telepot
import urllib3

proxy_url = "http://54.93.207.193:80"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = './webhook_pkey.pem'
bot = telepot.Bot('971158672:AAFt3SgFEtM2YEfqOixJeHoslEyleKV3iQY')
bot.setWebhook("https://USER_NAME.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        if text == "/start":
            bot.sendMessage(chat_id, 'Ты вызвал команду Тест')
        else:
            bot.sendMessage(chat_id, 'Ты пишешь какие то буквы')
    return "OK"