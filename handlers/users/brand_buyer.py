from aiogram.dispatcher import FSMContext

from data.texts import texts, user_menu_text
from keyboards.inline.categories import influencers_seller_categories
from loader import dp


@dp.callback_query_handler(lambda call: call.data == "brand_buyer")
async def influencers(call, state: FSMContext):
    async with state.proxy() as data:
        await call.message.edit_text(
            texts[data["lang"]]["captions_category"],
            reply_markup=await influencers_seller_categories(data["lang"]),
        )
