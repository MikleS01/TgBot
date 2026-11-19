from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import CallbackQuery

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Депай!", callback_data="btn_dep",style="success",icon_custom_emoji_id="5821077289185578407"),
       
    ],
    [
        InlineKeyboardButton(text="Играть", callback_data="btn_play",style="primary",icon_custom_emoji_id="5843973184314937720"),
        InlineKeyboardButton(text="Вывод", callback_data="btn3_w",style="danger", icon_custom_emoji_id="5843973184314937720")

    ]
])
dodep_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Деп по СБП", callback_data="btn_sbp",style="success"),
        InlineKeyboardButton(text="МИP/VISA", callback_data="btn_visa",style="success"),
        InlineKeyboardButton(text="TRC-20", callback_data="btn_crypto",style="success")
    ],
    [
        InlineKeyboardButton(text="Назад в меню", callback_data="btn_menu",style="danger",icon_custom_emoji_id="5843680709926981861")
    ]
])

game_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="В upgrade", callback_data="btn_upgrade")   
    ],
    [
        InlineKeyboardButton(text="Кейсы", callback_data="btn_case")      
    ],
    [
        InlineKeyboardButton(text="Контракт", callback_data="btn_contract")
    ],
    [
        InlineKeyboardButton(text="Назад в меню", callback_data="btn_menu",style="danger",icon_custom_emoji_id="5843680709926981861")
    ]
])