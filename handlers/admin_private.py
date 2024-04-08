from aiogram import F, Router, types, Bot
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import orm_change_banner_image, orm_get_info_pages
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


################# Микро FSM для загрузки/изменения баннеров ############################


class AddBanner(StatesGroup):
    image = State()

# Отправляем перечень информационных страниц бота и становимся в состояние отправки photo
@admin_router.message(StateFilter(None), F.text == 'Добавить/Изменить баннер')
async def add_image2(message: types.Message, state: FSMContext, session: AsyncSession):
    pages_names = [page.name for page in await orm_get_info_pages(session)]
    await message.answer(f"Отправьте фото баннера.\nВ описании укажите для какой страницы:\
                         \n{', '.join(pages_names)}")
    await state.set_state(AddBanner.image)

# Добавляем/изменяем изображение в таблице (там уже есть записанные страницы по именам:
# main, catalog, cart(для пустой корзины), about, payment, shipping
@admin_router.message(AddBanner.image, F.photo)
async def add_banner(message: types.Message, state: FSMContext, session: AsyncSession):
    image_id = message.photo[-1].file_id
    for_page = message.caption.strip()
    pages_names = [page.name for page in await orm_get_info_pages(session)]
    if for_page not in pages_names:
        await message.answer(f"Введите нормальное название страницы, например:\
                         \n{', '.join(pages_names)}")
        return
    await orm_change_banner_image(session, for_page, image_id,)
    await message.answer("Баннер добавлен/изменен.")
    await state.clear()

# ловим некоррекный ввод
@admin_router.message(AddBanner.image)
async def add_banner2(message: types.Message, state: FSMContext):
    await message.answer("Отправьте фото баннера или отмена")


@admin_router.message(F.photo)
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
