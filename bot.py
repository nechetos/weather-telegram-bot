from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Привет! Я погодный бот ☀️")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if name == "main":

    main()
