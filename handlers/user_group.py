import asyncio
import os
import random

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, MagicData

user_group_router = Router()

username = "vvt48"

vocab = ["Суки!", "Черти!", "Уроды!", "Ненавижу!", "Чмо!"]

quotes = ["-Витек, нам налево! -Я знаю, я поехал направо!", "Мы на мячике поедем?", "Маленький ребенок с большим сердцем!",
          "Слуха, как у жопи ухо!", ]


@user_group_router.message(F.text.lower().contains('зда') | F.text.lower().contains('при') | F.text.lower().contains("hi")
                              | F.text.lower().contains('дро'))
async def base(message: types.Message):
    await message.answer("Здарова, " + message.from_user.full_name + ", ёпрст!")


@user_group_router.message(F.text.lower().contains('как') | F.text.lower().contains('сам') | F.text.lower().contains("дел")
                           | F.text.lower().contains('жиз'))
async def base(message: types.Message):
    await message.answer("Нормально! А ты как, " + message.from_user.full_name + "?")


@user_group_router.message()
async def base(message: types.Message):
    if message.from_user.username == username:
        await message.delete()
        reply = random.choice(vocab)
        await message.answer(reply)
