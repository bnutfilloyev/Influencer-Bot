from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from data.texts import texts
from keyboards.inline.categories import user_menu_keyboard
from loader import dp
from utils.db_api import users


@dp.message_handler(content_types=ContentType.CONTACT)
async def get_phone_number(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        users.update_one(
            {"user_id": msg.from_user.id},
            {"$set": {"phone_number": msg.contact.phone_number}},
            upsert=True,
        )
        data["lang"] = users.find_one({"user_id": msg.from_user.id})["lang"]
        await msg.answer(
            texts[data["lang"]]["start"],
            reply_markup=await user_menu_keyboard(data["lang"]),
        )
