if __name__ == '__main__':
    from aiogram import executor
    from src import dp
    executor.start_polling(dp, skip_updates=True)