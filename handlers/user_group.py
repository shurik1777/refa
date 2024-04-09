from aiogram import Bot, types, Router
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
user_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))


@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()


"""
1. from aiogram import F, Bot, types, Router - импортируем необходимые модули из библиотеки Aiogram.
 Здесь F используется для фильтрации сообщений, Bot является классом для создания бота, 
 types содержит типы данных для работы с сообщениями, а Router используется для создания маршрутизации сообщений.

2. from aiogram.filters import Command - импортируем фильтр Command, который позволяет обрабатывать команды,
 начинающиеся со знака /.

3. from filters.chat_types import ChatTypeFilter - импортируем фильтр ChatTypeFilter, 
который позволяет фильтровать сообщения по типу чата (группа, супергруппа).

4. user_group_router = Router() - создаем экземпляр класса Router, 
который будет использоваться для маршрутизации сообщений в группах и супергруппах.

5. user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup'])) - добавляем фильтр 
к маршруту сообщений (message), чтобы он пропускал только те сообщения, которые приходят из групп или супергрупп.

6. user_group_router.edited_message.filter(ChatTypeFilter(['group', 'supergroup'])) - аналогично, добавляем фильтр
 к маршруту редактированных сообщений (edited_message).

7. @user_group_router.message(Command("admin")) - декоратор, который указывает, 
что функция get_admins должна вызываться при получении команды "/admin".

8. async def get_admins(message: types.Message, bot: Bot) - определение асинхронной функции get_admins,
 которая принимает объект сообщения types.Message и экземпляр бота Bot.

9. Внутри функции get_admins происходит следующее:
   - Получаем ID чата, в котором было отправлено сообщение.
   - Запрашиваем список администраторов чата у бота.
   - Фильтруем полученный список, оставляя только тех пользователей, у которых статус "creator" или "administrator".
   - Сохраняем отфильтрованный список администраторов в атрибуте бота bot.my_admins_list.
   - Если отправитель сообщения находится в списке администраторов, удаляем сообщение.

Таким образом, данный код позволяет создать бота,
 который может определять администраторов в группах и супергруппах Telegram и удалять сообщения,
  отправленные этими администраторами.
  
Взаимосвязь между user_group и chat_types кода заключается в том,
 что первая часть использует определённые фильтры (в частности, ChatTypeFilter) для маршрутизации сообщений,
  а вторая часть определяет эти фильтры и их поведение.
"""
