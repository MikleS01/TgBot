from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📊 Математика',style="danger")],
    [KeyboardButton(text='👁 Тeкст',style="primary")],
],
resize_keyboard=True)