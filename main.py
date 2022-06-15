# import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='5181589760:AAHdU5ZJZ9IhTZqTzmH0_VIzVgOQY64CRDo', use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, World")

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()