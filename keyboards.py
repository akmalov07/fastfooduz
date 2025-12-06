from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from database import BRANCHES

# Asosiy menyu
main_menu_admin = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍔 Menyu")],
        [KeyboardButton(text="➕ Category qo'shish"), KeyboardButton(text="➕ Product qo'shish")],
        [KeyboardButton(text="➖ Category o'chirish"), KeyboardButton(text="➖ Product o'chirish")],
        [KeyboardButton(text="👥 Foydalanuvchilar")],
    ],
    resize_keyboard=True
)

admin_ha_yoq_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Ha"), KeyboardButton(text="❌ Yo'q")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍔 Menyu"), KeyboardButton(text="🛒 Mening Savatim")],
        [KeyboardButton(text="⚙️ Sozlamalar"), KeyboardButton(text="🏪 Filliallarimiz")],
        [KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)

# Sozlamalar uchun inline keyboard (til tanlash)
language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")
        ]
    ]
)

# Filliallar uchun keyboard
branches_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=name)] for name in BRANCHES],
    resize_keyboard=True
)

from database import get_all_categories


kategory_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=category[1])] for category in get_all_categories()
    ] + [[KeyboardButton(text="⬅️ Orqaga")]],
    resize_keyboard=True
)
