from bot import UserState, dp, bot
from aiogram.utils.markdown import text, bold
from aiogram.types import Message, ParseMode
from random import randint

from src.store.store_worker import User, open_store, write_store
from src.callback_handler.on_hub_handler import handler as hub_handler

@dp.message_handler(commands=["g"], state=UserState.Hub.Main)
async def on_generate_secrete_santa(message: Message):
    if message.from_user.id == 365913711:

        def get_random_user_id(users_id):
            random_index = randint(0, len(users_id)-1)
            return users_id[random_index]

        def check_unic_user(santa, user_id):
            answer = True
            for key in santa:
                if santa[key]["id"] == user_id:
                    answer = False
            return answer

        def give_user_to_user(users):
            on_secret_santa = open_store().on_secret_santa
            for user_id in users:
                while True:
                    your_user_id = get_random_user_id([key for key in users])
                    if str(users[your_user_id]["id"]) != str(users[user_id]["id"]):
                        if check_unic_user(on_secret_santa, your_user_id):
                            on_secret_santa[user_id] = users[your_user_id]
                            break
            return on_secret_santa

        store = open_store()
        on_secret_santa = give_user_to_user(store.users)
        store = store._replace(on_secret_santa=on_secret_santa)
        write_store(store)
        names = ["твое солнышко", "твой бедолага", "твой геймер", "твой репер", "твой клоун"]
        for key in on_secret_santa:
            await bot.send_photo(
                chat_id=key,
                photo=on_secret_santa[key]["photo_url"],
                caption=text(
                    f"А вот и {names[randint(0, len(names) - 1)]}, которому тебе придется дарить подарок🧑🏻‍🎄🎁",
                    f"\n\nЗовут этого (🤡) -> {on_secret_santa[key]['name']}"
                    f"\nУ него есть пожелания... ну что бы ему хотелось, он просил передать тебе: {on_secret_santa[key]['wishlist']}",
                    f"\n\nА вот этого ему бы точно не хотелось🏜️: {on_secret_santa[key]['hatelist']}",
                )
            )
            