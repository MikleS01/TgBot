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

load_dotenv()
data = []

tg_bot_token = os.getenv("TOKEN")
dp = Dispatcher(storage=MemoryStorage())

class States(StatesGroup):
    waiting_name = State()
    waiting_age = State()
    waiting_aprovement = State()
@dp.message(F.text=="/start")
async def main(message: Message, state: FSMContext):
    await message.answer("Пройдите регистрацию")
    await message.answer(States.waiting_aprovement)
@dp.message(States.waiting_aprovement)
async def name(message: Message, state: FSMContext):
    await message.answer("введите имя")
    await state.set_state(States.waiting_name)

@dp.message(States.waiting_name)
async def age(message: Message, state: FSMContext):
    await message.answer("введите возраст")
    await state.set_state(States.waiting_age)
    await message.answer("Вcе данные введены")
    temp_data = await state.get_data()
    data.append(temp_data["first_name"])
    data.append(temp_data["second_name"])
    data.append(message.text)
    await message.answer("Все данные введены")
    await state.clear() 



async def main():
    bot = Bot(token=tg_bot_token)

    await dp.start_polling(bot)


   

if __name__ == "__main__":
    asyncio.run(main())



