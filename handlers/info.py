from aiogram import Router, types
from aiogram.filters import Command

info_router = Router()

@info_router.message(Command("myinfo"))
async def send_info(message: types.Message) -> None:
    user_id: int = message.from_user.id
    first_name: str = message.from_user.first_name
    username: str = message.from_user.username if message.from_user.username else 'Нет'
    info_message: str = (f"Ваш id: {user_id}\n"
                         f"Ваше имя: {first_name}\n"
                         f"Ваш юзернейм: {username}")
    await message.reply(info_message)