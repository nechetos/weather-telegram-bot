import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8165242190:AAGGwSR8oh0oBdtJkIkglIbtAmDBlZG2qfE"
WEATHER_API_KEY = "f3cc9a774ce15cad663ced259bf571af"
CITY = "Yekaterinburg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот погоды ☀️\nНапиши /weather — пришлю текущую погоду."
    )

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    r = requests.get(url)
    data = r.json()
    if r.status_code != 200:
        await update.message.reply_text("Не удалось получить погоду 😢")
        return
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    await update.message.reply_text(f"🌡 Температура: {temp}°C\n☁️ Погода: {desc}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))
    app.run_polling()

if name == "main":
    main()
