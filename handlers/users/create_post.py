from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.types.callback_query import CallbackQuery

from states.States import Form


@dp.callback_query_handler(text_contains='video')
async def create_video_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer()
        await Form.post.set()


@dp.callback_query_handler(text_contains='photo')
async def create_video_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer()
        await Form.post.set()


@dp.callback_query_handler(text_contains='text')
async def create_video_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.answer()
        await Form.post.set()


@dp.message_handler(state=Form.post)
async def create_post(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post'] = msg.text
        # thanking message
