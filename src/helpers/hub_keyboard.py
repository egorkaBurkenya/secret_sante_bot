from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = [
        [
            InlineKeyboardButton(text="xочу другое имя", callback_data="change_name"),
            InlineKeyboardButton(text="новое фото🤡", callback_data="change_photo"),
        ],
        [
            InlineKeyboardButton(text="хочу изменить wishlist", callback_data="change_wishlist"),
            InlineKeyboardButton(text="хочу изменить hatelist", callback_data="change_hatelist")
        ]
    ]


hub_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)