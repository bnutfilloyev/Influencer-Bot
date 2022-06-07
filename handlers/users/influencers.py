from aiogram.dispatcher import FSMContext

from data.texts import inf_cat_check, influencers_category, texts, user_menu_text
from keyboards.inline.categories import (
    influencers_seller_categories,
    services_categories,
)
from loader import dp


@dp.callback_query_handler(lambda call: call.data == "influencers")
async def influencers(call, state: FSMContext):
    async with state.proxy() as data:
        await call.message.edit_text(
            texts[data["lang"]]["captions_category"],
            reply_markup=await influencers_seller_categories(data["lang"]),
        )


@dp.callback_query_handler(lambda call: call.data in inf_cat_check)
async def influencers_category_handler(call, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = call.data
        await call.message.edit_text(
            texts[data["lang"]]["services_category"],
            reply_markup=await services_categories(data["lang"]),
        )


@dp.callback_query_handler(text_contains="create")
async def create_influencer(call, state: FSMContext):
    pass


@dp.callback_query_handler()
async def callback_handler(call, state: FSMContext):
    print(call.data)
    print(call.data in list(influencers_category.popitem()[-1].keys()))
