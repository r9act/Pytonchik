import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv

from handlers.user_group import user_group_router

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router

ALLOWED_UPDATES = "message, edited_message"

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=[ALLOWED_UPDATES])


asyncio.run(main())
