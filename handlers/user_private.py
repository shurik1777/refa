from random import randint

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from asyncpg import Path
from aiogram import Bot

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


@user_private_router.message(F.photo)
async def photo_cmd(message: types.Message, bot: Bot):
    await message.answer('Спасибо за фото! Если это котик и фотография понравится Богу котячьего рандома, '
                         'то он рано или поздно попадет в подборку!')
    foto_ = message.photo[-1]
    global count
    count += 1
    await bot.download(
        foto_,
        destination=f"C:\\Users\\shuri\\OneDrive\\Рабочий стол\\rrr\\WeddingBot\\image\\image_{count}.jpg"
    )
