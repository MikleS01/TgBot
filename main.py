import asyncio
import os 
from dotenv import load_dotenv 
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
load_dotenv()
tg_bot_token = os.getenv("TOKEN")
print(tg_bot_token)
dp = Dispatcher()


@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет! Это первое сообщение ")

@dp.message(F.text=="/donat")
async def command_donate(message: Message) -> None:
    await message.answer("Привет! Гони деньги мудила")

async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())