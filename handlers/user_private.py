import asyncio
import os
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, MagicData

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Здарова, это Витёк")


@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("Вот че могу:")


@user_private_router.message(Command("me"))
async def menu_cmd(message: types.Message):
    await message.answer("Вот че могу:")


@user_private_router.message(Command("pizd"))
async def menu_cmd(message: types.Message):
    await message.answer("Вот че могу:")


@user_private_router.message(Command("show"))
async def menu_cmd(message: types.Message):
    await message.answer("Вот че могу:")


@user_private_router.message(F.text.lower() == "var")
async def base(message: types.Message):
    await message.answer("Magic filter")


@user_private_router.message(Command("pizd"))
async def base(message: types.Message):
    await message.answer("Здарова, " + message.from_user.full_name + ", ебать!")

