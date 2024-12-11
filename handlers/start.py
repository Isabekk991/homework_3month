from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def send_welcome(message: types.Message) -> None:
    first_name: str = message.from_user.first_name
    await message.reply(f"Привет, {first_name}! Добро пожаловать в наше кафе. Чем могу помочь?")

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review"),
            ],

        ]
    )