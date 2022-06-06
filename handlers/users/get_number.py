from loader import dp
from aiogram import types
from aiogram.types import ContentType

from utils.db_api import users


@dp.message_handler(content_types=ContentType.CONTACT)
async def get_phone_number(msg: types.Message):
    user = users.update_one({'user_id': msg.from_user.id}, {'$set': {'phone_number': msg.contact.phone_number}}, upsert=True)
    print(user.raw_result)