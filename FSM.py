from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import Message, BotCommand
from aiogram import Bot, Dispatcher, F
import asyncio
import os 
from dotenv import load_dotenv 

load_dotenv()
tg_bot_token = os.getenv("TOKEN")
dp = Dispatcher()

print("привеет ")
class States(StatesGroup):
    waiting_first_name = State()
    waiting_second_name = State()
    waiting_third_name = State()

@dp.message(F.text=="/better")
async def better(message: Message, state: FSMContext):
    await message.answer("Введите первое имя")
    await state.set_state(States.waiting_first_name)

@dp.message(States.waiting_first_name)
async def first_name(message: Message, state: FSMContext):
    await message.answer("Введите второе имя")
    await state.set_state(States.waiting_second_name)

@dp.message(States.waiting_second_name)
async def second_name(message: Message, state: FSMContext):
    await message.answer("Введите третье имя")
    await state.set_state(States.waiting_third_name)

@dp.message(States.waiting_third_name)
async def third_name(message: Message, state: FSMContext):
    await message.answer("Вcе имена введены")




async def main():
    bot = Bot(token=tg_bot_token)

    await dp.start_polling(bot)


   

if __name__ == "__main__":
    asyncio.run(main())



