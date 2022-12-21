import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from src.state.state import _UserState

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN if API_TOKEN != None else "token dont found")
dp = Dispatcher(bot, storage=MemoryStorage())
UserState = _UserState()