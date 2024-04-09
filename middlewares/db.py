from typing import Callable, Dict, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from sqlalchemy.ext.asyncio import async_sessionmaker


class DataBaseSession(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.session_pool() as session:
            data['session'] = session
            return await handler(event, data)


"""
Данный код представляет собой часть Middleware для бота на базе библиотеки Aiogram,
 который использует SQLAlchemy для взаимодействия с базой данных.
  Middleware в контексте Aiogram - это набор вспомогательных функций,
   которые могут модифицировать данные перед тем, как они будут обработаны основным обработчиком.

Вот что делает каждый элемент кода:

1. from typing import Callable, Dict, Awaitable, Any: Импорт типов из модуля typing,
 которые будут использоваться для аннотации параметров функций.

2. from aiogram import BaseMiddleware, TelegramObject: Импорт базового класса Middleware
 и общего предка всех объектов, передаваемых через API Telegram.

3. from sqlalchemy.ext.asyncio import async_sessionmaker: Импорт фабрики сессий
 для асинхронного использования с SQLAlchemy.

4. class DataBaseSession(BaseMiddleware): Определение класса DataBaseSession,
 который наследуется от BaseMiddleware. Этот класс будет использоваться
  для предоставления доступа к базе данных в рамках обработки событий.

5. def __init__(self, session_pool: async_sessionmaker): Конструктор класса DataBaseSession,
 который принимает фабрику сессий (session_pool) для создания новых сессий с базой данных.

6. async def __call__(self, handler: 
Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject, data: Dict[str, Any]) -> Any:
 Метод __call__ класса DataBaseSession, который является точкой входа для middleware.
  Он принимает функцию-обработчик (handler), событие (event) и словарь данных (data),
   которые будут переданы обработчику. Метод возвращает результат выполнения обработчика.

7. async with self.session_pool() as session: Блокировка сессии базы данных с помощью фабрики сессий.
 Сессия создаётся внутри блока async with, что гарантирует её закрытие после выхода из блока.

8. data['session'] = session: Добавление ссылки на текущую сессию в словарь данных,
 чтобы она была доступна обработчику.

9. return await handler(event, data): Вызов функции-обработчика с событием и данными,
 включая ссылку на сессию базы данных.

Таким образом, данный код создаёт middleware,
 который предоставляет доступ к базе данных в рамках обработки событий ботом.
"""