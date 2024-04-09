from aiogram.filters import Filter
from aiogram import Bot, types


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool:
        return message.from_user.id in bot.my_admins_list


"""
Класс ChatTypeFilter наследуется от Filter и представляет собой фильтр,
 который проверяет тип чата (группа или супергруппа), в котором было отправлено сообщение.
  Метод __call__ возвращает True, если тип чата соответствует одному из переданных в конструкторе типов.

Класс IsAdmin также наследуется от Filter и представляет собой фильтр,
 который проверяет, является ли пользователь, отправивший сообщение, администратором чата.
  Для этого он проверяет, содержится ли ID пользователя в списке администраторов,
   который хранится в атрибуте bot.my_admins_list.
"""