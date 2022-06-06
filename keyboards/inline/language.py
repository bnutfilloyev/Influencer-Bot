from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import LanguageCallbackData

lang_list = [
    [
        InlineKeyboardButton(text="🇺🇸 English", callback_data=LanguageCallbackData.new('en')),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data=LanguageCallbackData.new('ru')),
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data=LanguageCallbackData.new('uz')),
    ]
]

language_keyboard = InlineKeyboardMarkup(inline_keyboard=lang_list)
