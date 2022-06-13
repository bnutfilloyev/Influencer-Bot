from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.texts import select_lang, texts
from keyboards.inline.categories import user_menu_keyboard
from keyboards.inline.language import language_keyboard
from loader import dp
from utils.db_api import users


@dp.message_handler(CommandStart(), state="*")
async def bot_start(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if users.find_one({"user_id": msg.from_user.id}) is None:
            await msg.answer(select_lang["select_lang"], reply_markup=language_keyboard)
            users.insert_one(
                {"user_id": msg.from_user.id, "lang": msg.from_user.language_code}
            )
            return
        lang = users.find_one({"user_id": msg.from_user.id})["lang"]
        data['lang'] = lang
        await msg.answer(texts[lang]["start"], reply_markup=await user_menu_keyboard(lang))