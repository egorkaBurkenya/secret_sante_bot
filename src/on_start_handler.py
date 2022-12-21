from bot import dp, UserState
from aiogram.utils.markdown import text, bold
from aiogram.types import Message, ParseMode

@dp.message_handler(commands=["start"], state=None)
async def on_start_handler(message: Message):
    """
    Функция реагирующая на ввод команды \\start \n
    отправляя преветсвенное сообщение пользователю.
    """
    await message.delete()
    await message.answer(
        text(
            bold("Secret Santa 🧑🏻‍🎄🎁"),
            "\n\nЭто бот тайного санты\\!",
            "\nно пока он работает только для ребят с gmsGang",
            "\nпоэтому если ты не один из нас", 
            "\nзайти у тебя не выйдет \\-\\> Лох",
            "\n\nА если ты один из нас, то вводи пароль🔑:"
        ),
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await UserState.Registration.WatingPassword.set()
