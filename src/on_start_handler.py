from bot import dp, UserState
from aiogram.utils.markdown import text, bold
from aiogram.types import Message, ParseMode

from src.store.store_worker import User, open_store
from src.callback_handler.on_hub_handler import handler as hub_handler

def checking_that_the_user_is_already_in_the_store(handler):
    async def handler_with_checking(message: Message):
        store = open_store()
        already_in_the_store=False
        for id in store.users:
            print(id)
            if int(message["chat"]["id"]) == int(id):
                already_in_the_store = True
        if already_in_the_store:
            user_json = store.users[str(message["chat"]["id"])]
            user = User(
                id=user_json["id"],
                username=user_json["username"],
                name=user_json["name"],
                photo_url=user_json["photo_url"],
                wishlist=user_json["wishlist"],
                hatelist=user_json["hatelist"]
            )
            print(user)
            await hub_handler(message, user)
            await UserState.Hub.Main.set()
        else:
            await handler(message)
    return handler_with_checking

@dp.message_handler(commands=["start"], state=None)
@checking_that_the_user_is_already_in_the_store
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
