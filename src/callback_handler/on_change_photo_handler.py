from bot import dp, bot, UserState
from aiogram.utils.markdown import text, bold, italic
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import text, bold, italic

from src.helpers.hub_keyboard import hub_keyboard
from src.helpers.delete_messages import delete_messages_for_count

from src.store.store_worker import get_user_by_id_from_store, edit_user_props_in_store

@dp.callback_query_handler(text_contains="change_photo", state=UserState.Hub.Main)
async def on_change_name_callback_handler(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Отправте новое фото: ")
    await UserState.Hub.ChangePhoto.set()

@dp.message_handler(content_types=["photo"], state=UserState.Hub.ChangePhoto)
async def on_get_name_handler(message: Message):
    await delete_messages_for_count(message, bot)
    photo_url = message.photo[-1].file_id
    user = get_user_by_id_from_store(int(message["chat"]["id"]))
    user = user._replace(photo_url=photo_url)
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
        photo=photo_url,
        caption=_message,
        reply_markup=hub_keyboard
    )    
    await UserState.Hub.Main.set()
