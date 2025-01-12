from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


tarjimon_klaviyatura = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="avto-uz", callback_data="avto")],
        [InlineKeyboardButton(text="uz-en 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data="en"), InlineKeyboardButton(text="uz-ru 🇷🇺", callback_data="ru")]
    ]
)


asosiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Wikipediya", callback_data="wiki"), InlineKeyboardButton(text="Tarjimon", callback_data='tarjima')]
    ]
)


asosiy2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True

)
