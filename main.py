import os
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
import handlers.info
from handlers.menu import menu_router
from handlers.other_message import echo_router
from handlers.picture import picture_router
from handlers.start import start_router
from dotenv import load_dotenv
from handlers.dialog import dialog_router


load_dotenv()

API_TOKEN = os.getenv('7916062297:AAEhmcyZU7A5WPj318g982Zavk1EJwfqKLs')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()



dp.include_router(start_router)
dp.include_router(handlers.info.info_router)
dp.include_router(menu_router)
dp.include_router(echo_router)
dp.include_router(picture_router)
dp.include_router(dialog_router)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)