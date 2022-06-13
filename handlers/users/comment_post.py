from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data.texts import texts
from keyboards.inline.categories import comment_post_categories
from loader import dp
from states.States import Form


@dp.callback_query_handler(text_contains="comment")
async def comment_influencer(call, state: FSMContext):
    async with state.proxy() as data:
        # For get location
        # if users.find_one({"user_id": call.from_user.id}).get("location", False):
        #     await call.message.edit_text(
        #         texts[data["lang"]]["location_question"],
        #         reply_markup=await create_post_categories(data["lang"]),
        #     )

        await call.message.edit_text(
            texts[data["lang"]]["comment_post"],
            reply_markup=await comment_post_categories(data["lang"]),
        )
        await Form.comment.set()


@dp.callback_query_handler(state=Form.comment)
async def comment_num(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        # for DEBUG
        await call.message.answer(call.data)
        await call.message.answer(texts[data['lang']]['comment_post'])
        await Form.post.set()


@dp.message_handler(state=Form.post)
async def create_post(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['post'] = msg.text
        await msg.answer("Done")
