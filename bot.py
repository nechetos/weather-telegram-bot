import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8165242190:AAGGwSR8oh0oBdtJkIkglIbtAmDBlZG2qfE"

WEATHER_API_KEY = "f3cc9a774ce15cad663ced259bf571af"
CITY = "Yekaterinburg"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот погоды ☁️\n"
        "Напиши /weather — пришлю прогноз."
    )


@dp.message(Command("weather"))
async def weather(message: types.Message):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    )

    r = requests.get(url)
    data = r.json()

    if r.status_code != 200:
        await message.answer("Не удалось получить погоду 😢")
        return

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    await message.answer(
        f"🌡 Температура: {temp}°C\n"
        f"☁️ Погода: {desc}"
    )


async def main():
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())
