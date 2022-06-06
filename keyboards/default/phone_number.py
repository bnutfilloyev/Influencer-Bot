from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.texts import texts, user_menu_text
from utils.db_api import users


async def phone_number_keyboard(lang):
    get_phone_number = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=texts[lang]['phone_number_button'],
                           request_contact=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
    return get_phone_number


async def user_menu_keyboard(lang):
    user_menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=user_menu_text[lang]['influencers']),
            KeyboardButton(text=user_menu_text[lang]['brand_buyer']),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
    return user_menu
