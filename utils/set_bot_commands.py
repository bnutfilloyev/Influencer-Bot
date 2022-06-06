from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Runing bot"),
            types.BotCommand("help", "Help"),
            types.BotCommand("language", "Change language"),
        ]
    )
