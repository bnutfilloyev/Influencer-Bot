from aiogram import types
from aiogram.dispatcher import FSMContext

from data.texts import texts
from keyboards.inline.categories import create_post_categories
from loader import dp
from aiogram.types.callback_query import CallbackQuery

from states.States import Form


@dp.callback_query_handler(text_contains="create")
async def create_influencer(call, state: FSMContext):
    async with state.proxy() as data:
        # For get location
        # if users.find_one({"user_id": call.from_user.id}).get("location", False):
        #     await call.message.edit_text(
        #         texts[data["lang"]]["location_question"],
        #         reply_markup=await create_post_categories(data["lang"]),
        #     )

        await call.message.edit_text(
            texts[data["lang"]]["create_post"],
            reply_markup=await create_post_categories(data["lang"]),
        )


@dp.callback_query_handler(text_contains='video')
async def create_video_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer(texts[data['lang']]['video_post'])
        await Form.post.set()


@dp.callback_query_handler(text_contains='photo')
async def create_video_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer(texts[data['lang']]['photo_post'])
        await Form.post.set()


@dp.callback_query_handler(text_contains='text')
async def create_video_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer(texts[data['lang']]['text_post'])
        await Form.post.set()


@dp.message_handler(state=Form.post)
async def create_post(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post'] = msg.text
        await state.finish()
