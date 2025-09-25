import os
import random
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.types import FSInputFile

# Замените на токен вашего бота от @BotFather
API_TOKEN = "7753255667:AAH22vasZeB5rwTucCUDbnbvr5R5xTthbJs"

# Инициализация бота
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Клавиатура
button = KeyboardButton(text="🤓 Умный человек в очках скачать обои")
kb = ReplyKeyboardMarkup(
    keyboard=[[button]],
    resize_keyboard=True
)

IMAGE_DIR = "images"

@dp.message(Command("start"))
async def start_command(message: types.Message):
    print("Команда /start получена")  # Отладка
    await message.answer("Привет! Нажми кнопку ниже 👇", reply_markup=kb)

@dp.message(F.text == "🤓 Умный человек в очках скачать обои")
async def send_random_image(message: types.Message):
    print("Кнопка нажата, начинаю обработку")  # Отладка
    files = os.listdir(IMAGE_DIR)
    print("Файлы в папке:", files)  # Отладка
    if not files:
        print("Папка пуста")  # Отладка
        await message.answer("Папка с картинками пуста 😔")
        return

    random_file = random.choice(files)
    file_path = os.path.join(IMAGE_DIR, random_file)
    print("Отправляем файл:", file_path)  # Отладка

    try:
        photo = FSInputFile(file_path)
        print("Файл открыт, отправляю фото")  # Отладка
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        print("Фото отправлено")  # Отладка
    except Exception as e:
        print(f"Ошибка: {str(e)}")  # Отладка
        await message.answer(f"Ошибка при отправке: {str(e)}")

async def main():
    print("Бот запущен, начинаю polling")  # Отладка
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())