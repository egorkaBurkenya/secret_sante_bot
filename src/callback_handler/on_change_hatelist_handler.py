from bot import dp, bot, UserState
from aiogram.utils.markdown import text, bold, italic
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import text, bold, italic

from src.helpers.hub_keyboard import hub_keyboard
from src.helpers.delete_messages import delete_messages_for_count

from src.store.store_worker import get_user_by_id_from_store, edit_user_props_in_store
from src.callback_handler.on_hub_handler import handler

@dp.callback_query_handler(text_contains="change_hatelist", state=UserState.Hub.Main)
async def on_change_hatelist_callback_handler(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Введи новые пожелания: ")
    await UserState.Hub.ChangeHateList.set()

@dp.message_handler(content_types=["text"], state=UserState.Hub.ChangeHateList)
async def on_get_hatelist_handler(message: Message):
    await delete_messages_for_count(message, bot)
    hatelist = message.text
    user = get_user_by_id_from_store(int(message["chat"]["id"]))
    user = user._replace(hatelist=hatelist)
    _message = ""
    if edit_user_props_in_store(user):
        _message = text(
            f"Ты Бедолага, тебя зовут: ",
            bold(user.name),
            italic(f"\n\nхочешь: "),
            user.wishlist,
            italic(f"\n\nне хочешь: "),
            user.hatelist
        ) 
    else:
        _message = text(
            "🛑🛑🛑Что-то пошло не так, напиши егору🛑🛑🛑\n\n"
            f"Ты Бедолага, тебя зовут: ",
            bold(user.name),
            italic(f"\n\nхочешь: "),
            user.wishlist,
            italic(f"\n\nне хочешь: "),
            user.hatelist
        ) 
    await message.answer_photo(
        photo=user.photo_url,
        caption=_message,
        reply_markup=hub_keyboard
    )    
    await UserState.Hub.Main.set()
