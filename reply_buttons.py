from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📊 Кнопка 1',style="success",icon_custom_emoji_id="5438548621127615575")],
    [KeyboardButton(text='👁 Кнопка 3',style="primary",icon_custom_emoji_id="5382217586714902322")],
],
resize_keyboard=True)


    
