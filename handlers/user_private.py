from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command


from asyncpg import Path
from aiogram.types import FSInputFile
from random import randint

from sqlalchemy.ext.asyncio import AsyncSession

from handlers.menu_processing import get_menu_content

user_private_router = Router()
count = 0


# фича на возврат пользователю результирующую image из конкретной директории
# def choose_pic_Nikita_Igorevich():
#     return FSInputFile(f'image/{randint(1, len(list(Path("image").iterdir())))}.jpg')


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    media, reply_markup = await get_menu_content(session, level=0, menu_name="main")

    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)


@user_private_router.message(Command('menu', 'name'))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")
