from aiogram import Router, types
from aiogram.filters import Command
import random

menu_router = Router()

@menu_router.message(Command("menu"))
async def send_menu(message: types.Message) -> None:
    menu_items: str = "🍕 Меню:\n1. Пицца\n2. Бургер\n3. Салат\n4. Напитки"
    await message.reply(menu_items)

@menu_router.message(Command("random_dish"))
async def send_random_dish(message: types.Message) -> None:
    dishes: tuple = ("Пицца", "Бургер", "Суши", "Салат", "Паста")
    random_dish: str = random.choice(dishes)
    await message.reply(f"Случайное блюдо: {random_dish}")
