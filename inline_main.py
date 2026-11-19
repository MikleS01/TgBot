from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import Message, BotCommand
from aiogram import Bot, Dispatcher, F
import asyncio
import os 
from dotenv import load_dotenv 
from random import randint,choice
from aiogram.types import CallbackQuery
from inline_buttons import *

load_dotenv()

tg_bot_token = os.getenv("TOKEN")
print(tg_bot_token)
dp = Dispatcher()







@dp.message(F.text=="/start")
async def cmd_start(message: Message):
    await message.delete()
    await message.answer("Добро пожаловать в бота", reply_markup=main_menu)


@dp.callback_query(F.data == "btn_dep")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Нажата кнопка 1",reply_markup=dodep_menu)
    await callback.message.answer("Мама продай квартиру - пополнение")

async def main():
    bot = Bot(token=tg_bot_token)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())