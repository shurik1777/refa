from os import getenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.models import Base
from database.orm_query import orm_add_banner_description

from common.texts_for_db import categories, description_for_info_pages

engine = create_async_engine(getenv('DB_URL'), echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with session_maker() as session:
        # await orm_create_categories(session, categories)
        await orm_add_banner_description(session, description_for_info_pages)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


"""
Код выше содержит две функции: create_db и drop_db, 
которые используются для создания и удаления базы данных соответственно.
 Функция create_db создает базу данных, выполняя следующие шаги:

1. Создание асинхронного движка (create_async_engine) с URL,
 полученным из переменной окружения DB_URL. 
 Параметр echo=True включает вывод информации о выполняемых запросах в консоль.

2. Создание асинхронного сессионного производителя (async_sessionmaker),
 который связывается с созданным движком и использует класс AsyncSession.
  Параметр expire_on_commit=False предотвращает автоматическое обновление данных при каждом коммите транзакции.

3. Выполнение синхронизированного метода create_all из метаданных Base.metadata,
 который создает все таблицы, определенные в модели database.models.

4. Открытие сессии (session_maker) и вызов функции orm_add_banner_description,
 которая добавляет описания для информационных страниц в базу данных.

Функция drop_db выполняет обратное действие,
 удаляя все таблицы из базы данных с помощью метода drop_all из метаданных Base.metadata.

В данном коде используются асинхронные операции с базой данных,
 что позволяет выполнять несколько операций параллельно.
"""