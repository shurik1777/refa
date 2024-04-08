from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter, or_f

from filters.chat_types import ChatTypeFilter, IsAdmin

from kbds.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())

ADMIN_KB = get_keyboard(
    "Добавить картинку",
    "Все картинки квиза",
    "Добавить/Изменить баннер",
    placeholder="Выберите действие",
    sizes=(2,),
)


@admin_router.message(Command("admin"))
async def admin_features(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=ADMIN_KB)


@admin_router.message(F.text == "Добавить картинку")
async def chang_product(message: types.Message):
    await message.answer("Отправляй картинку")


@admin_router.message(F.text == "Все картинки квиза")
async def delete_product(message: types.Message):
    # async def delete_product(message: types.Message, counter):
    #     print(counter)
    await message.answer("Вот все картинки")


@admin_router.message(F.text == "Добавить/Изменить баннер")
async def chang_product(message: types.Message):
    await message.answer("Ты изменил баннер")
