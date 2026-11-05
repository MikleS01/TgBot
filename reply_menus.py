import asyncio
import os 
from dotenv import load_dotenv 
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import Message, BotCommand
from random import randint,choice
from aiogram.types import Message
from reply_buttons import main_menu_keyboard
load_dotenv()



tg_bot_token = os.getenv("TOKEN")
print(tg_bot_token)
dp = Dispatcher()


@dp.message(F.text=="/start")
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в бота", reply_markup=main_menu_keyboard)


@dp.message(F.entities)
async def cmd_start(message: Message):
    print(str(message.entities[0].custom_emoji_id))
    await message.answer(str(message.entities[0].custom_emoji_id))

    








async def main():
    bot = Bot(token=tg_bot_token)

    await dp.start_polling(bot)


   

if __name__ == "__main__":
    asyncio.run(main())
