import requests
from io import BytesIO

class TelegramSender:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_msg(self, msg):
        url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage'
        data = {"chat_id": self.chat_id, "text": msg}
        requests.post(url, data)

    def send_file(msg, filepath):
        token = telegram_bot
        url = f'https://api.telegram.org/bot{token}/sendDocument'
        chat_id = telegram_chat_id
        caption = msg
        document = {'document': open(filepath, 'rb')}
        data = {"chat_id": chat_id, "caption": caption}
        r = requests.post(url, data, files=document)
        print(r.text)


telegram_bot = None
telegram_chat_id = None

def set_credentials(bot_token, chat_id):
    global telegram_bot, telegram_chat_id
    telegram_bot = bot_token
    telegram_chat_id = chat_id

def send_msg(msg):
    if not telegram_bot or not telegram_chat_id:
        raise ValueError("You must call set_credentials() before using this function.")
    sender = TelegramSender(telegram_bot, telegram_chat_id)
    sender.send_msg(msg)

def send_file(msg, filepath):
    if not telegram_bot or not telegram_chat_id:
        raise ValueError("You must call set_credentials() before using this function.")
    sender = TelegramSender(telegram_bot, telegram_chat_id)
    sender.send_file(msg, filepath)