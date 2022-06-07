from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from data.texts import texts


async def phone_number_keyboard(lang):
    get_phone_number = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text=texts[lang]["phone_number_button"], request_contact=True
                )
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return get_phone_number
