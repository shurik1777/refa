from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command


from asyncpg import Path
from aiogram.types import FSInputFile
from random import randint

user_private_router = Router()
count = 0


# фича на возврат пользователю результирующую image из конкретной директории
# def choose_pic_Nikita_Igorevich():
#     return FSInputFile(f'image/{randint(1, len(list(Path("image").iterdir())))}.jpg')


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, я виртуальный помощник")


@user_private_router.message(Command('menu', 'name'))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")


