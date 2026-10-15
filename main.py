import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

tg_bot_token = "8708010020:AAGfBBcEKzdsQYwi7YkXd8Slb1dUYILnxHo"

dp = Dispatcher()


@dp.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет! Это первое сообщение бота! 1231123123123123123")


async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())