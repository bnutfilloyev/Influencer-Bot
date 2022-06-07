from aiogram import types

from data.texts import select_lang, texts
from keyboards.default.phone_number import phone_number_keyboard
from keyboards.inline.language import language_keyboard
from loader import dp
from utils.db_api import users


@dp.message_handler(commands=["language"])
async def change_lang(msg: types.Message):
    await msg.answer(select_lang["select_lang"], reply_markup=language_keyboard)


@dp.callback_query_handler(text_contains="language")
async def change_lang(call: types.CallbackQuery):
    lang = call.data.split(":")[1]
    users.update_one(
        {"user_id": call.from_user.id}, {"$set": {"lang": lang}}, upsert=True
    )
    if not users.find_one({"user_id": call.from_user.id}).get("phone"):
        await call.message.answer(
            texts[lang]["phone_number_button"],
            reply_markup=await phone_number_keyboard(lang),
        )
        return
    await call.message.edit_text(texts[lang]["change_lang_info"])
