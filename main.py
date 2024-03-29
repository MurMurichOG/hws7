import asyncio
from aiogram import types
import logging
from handlers.start import start_router
from hw4.bot import bot, dp
from hw4.shop import shop_router
from handlers.table import init, create, populate
from handlers.parser import parse_ads
from handlers.db import create_table, insert_data

async def on_startup():
    print('Online!')
    init()
    create()
    populate()

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало")
    ])
    dp.include_router(start_router)
    dp.include_router(shop_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


def main2():
    url = 'https://www.house.kg/snyat'
    ads_data = parse_ads(url)

    create_table()

    for ad in ads_data:
        insert_data(ad)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())