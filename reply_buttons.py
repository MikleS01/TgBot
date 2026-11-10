from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Математика',style="success",icon_custom_emoji_id="4974615152985899961")],
    [KeyboardButton(text=' Текст',style="primary",icon_custom_emoji_id="4974565219696116554")],
],
resize_keyboard=True)

math_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='*')],
    [KeyboardButton(text='+/-')],
    [KeyboardButton(text='Назад в меню')]
    
],
resize_keyboard=True)
    

text_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Назад в меню')]
    
],
resize_keyboard=True)