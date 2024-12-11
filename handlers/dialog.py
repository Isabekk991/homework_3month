from aiogram import Router, F, types
from aiogram.filters import Command, state
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


Review_router = Router()
class Review(StatesGroup):
    name = State()
    phone_number = State()
    food_rating  = State()
    extra_comments = State()


@Review_router.message(F.data == 'review')
async def start_review(message: types.Message, state: FSMContext):
    await message.answer("What's your name?")
    await state.set_state(Review.name)


@Review_router.message(Review.name)
async def start_review(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона?")
    await state.set_state(Review.phone_number)


@Review_router.message(Review.phone_number)
async def start_review(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Как оцениваете чистоту заведения?")
    await state.set_state(Review.food_rating)


@Review_router.message(Review.food_rating)
async def start_review(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Дополнительные комментарии...")
    await state.set_state(Review.extra_comments)
    await state.clear()
