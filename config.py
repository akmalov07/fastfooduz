import os
from dotenv import load_dotenv # pip install python-dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 364603275
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
