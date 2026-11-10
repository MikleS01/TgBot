from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Математика',style="success",icon_custom_emoji_id="4974615152985899961")],
    [KeyboardButton(text=' Текст',style="primary",icon_custom_emoji_id="4974565219696116554")],
],
resize_keyboard=True)

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='*',style="success")],
    [KeyboardButton(text='+/-',style="primary")],
    [KeyboardButton(text='Назад в меню',style="danger")]
    
],
resize_keyboard=True)
    

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='В главное меню',style="danger")]
    
],
resize_keyboard=True)