import time
import logging
import asyncio
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

TOKEN = ""
MSG = "Hello"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

db_connection = sqlite3.connect("scheduler.db")
db_cursor = db_connection.cursor()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Hello, {user_full_name}!")
    for i in range(7):
        await asyncio.sleep(60 * 60 * 24)
        await bot.send_message(user_id, MSG.format(user_name))

# @dp.message_handler(commands=['resource'])
# async def recourse_handler():
#
# @dp.message_handler(command=['book'])
# async def book_handler():

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
