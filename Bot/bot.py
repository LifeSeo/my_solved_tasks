from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
import logging

from random import randint as rnd

from config import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

disc = rnd(5, 50)

@dp.message_handler(commands=['start', "help"])
async def process_start_command(msg: types.Message):
    await msg.reply(f"Я бот. Приятно познакомиться, \
                               {msg.from_user.first_name}")

@dp.message_handler(content_types=["text"])
async def GetTextMessage(msg: types.Message, disc: int):
    if msg.text.lower() == "привет" or "hi":
        await msg.answer("Привет. Тебе неслыхано повезло, сейчас у нас Акция. \
                          Хочешь получить купон на скидку"  "?")
    else:
        await msg.answer("Привет. Меня первый раз так поприветствовали, \
                          но всеровно, тебе неслыханно повезло. Хочешь получить \
                          скидку"  "?")


if __name__ == '__main__':
    executor.start_polling(dp)
    



# @bot.message_handler(content_types=["text"])
# def get_text_massages(message):
#     if message.text == "Привет" or "Hi" or "Здравствуйте":
#         bot.send_message(message.from_user.id,
#                          "Привет. Тебе неслыхано повезло, сейчас у нас Акция. \
#                           Хочешь получить купон на скидку", discount, "?")
#     else:
#         bot.send_message(message.from_user.id,
#                          "Привет. Твое сообщение, не выглядит как приветствие, \
#                           но всеровно, тебе неслыханно повезло. Хочешь получить \
#                           скидку", discount, "?")

# bot.polling(none_stop=True, interval=0)