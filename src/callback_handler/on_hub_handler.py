from ast import Dict
from typing import Any, Coroutine
from bot import dp, bot, UserState
from aiogram.utils.markdown import text, bold, italic
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from src.helpers.hub_keyboard import hub_keyboard

from src.store.store_worker import add_new_user_to_store, User

async def handler(message: Message, data: User):
    _message = text(
        f"Ты Бедолага, тебя зовут: ",
        bold(data.name),
        italic(f"\n\nхочешь: "),
        data.wishlist,
        italic(f"\n\nне хочешь: "),
        data.hatelist
        )
    await message.answer_photo(photo=data.photo_url, caption=_message,
        reply_markup=hub_keyboard)
    

@dp.callback_query_handler(text_contains="hub", state=UserState.Hub.Main)
async def on_hub_callback_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.delete()
    user = User(
        id=int(call.message["chat"]["id"]),
        username=call.message.from_user.username,
        name=str(data.get("name")),
        photo_url=str(data.get("photo_url")),
        wishlist=str(data.get("wishlist")),
        hatelist=str(data.get("hatelist"))
    )
    await handler(call.message, user)
    add_new_user_to_store(user)
    # await state.finish()
    await call.message.delete()
    await UserState.Hub.Main.set()

