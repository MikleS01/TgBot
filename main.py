import asyncio
import os 
from dotenv import load_dotenv 
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import Message, BotCommand
from random import randint
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

@dp.message(F.text.startswith("/better")) 
async def command_num(message: Message) -> None:
    splited_message_text = message.text.split(" ")
    number1 = int(splited_message_text[1])
    number2 = int(splited_message_text[2])
    if number1 > number2:
        ans = number1
    else:
        ans = number2
    await message.answer(str(ans))


async def main():
    bot = Bot(token=tg_bot_token)
    await dp.start_polling(bot)

@dp.message(F.text.startswith("Мой возраст "))
async def command_age(message: Message):
    text = message.text.split(" ")
    age = int(text[2])
    new_age = age + 10
    await message.answer(f"через 10 лет тебе будет {new_age} лет")

@dp.message(F.text=="/random_nummber")
async def random_number(message: Message):
    a = randint(0,10)
    await message.answer(f"Ваше рандомное число от 0 до 10:{a}")




async def main():
    bot = Bot(token=tg_bot_token)

    await bot.set_my_commands([
        BotCommand(command="start", description="Начало"),
        BotCommand(command="donat", description="Донат"),
        BotCommand(command="better", description="Большее число"),
        BotCommand(command="random", description="Случайное имя"),
        BotCommand(command="random_number", description="Случайное число")
    ])

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
