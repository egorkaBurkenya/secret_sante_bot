from bot import dp, bot, UserState
from aiogram.utils.markdown import text, bold, italic
from aiogram.types import CallbackQuery, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

from src.helpers.hub_keyboard import hub_keyboard

@dp.callback_query_handler(text_contains="hub", state=UserState.Hub.Main)
async def on_hub_callback_handler(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    message = text(
        f"Ты Бедолага, тебя зовут: ",
        bold(data.get("name")),
        italic(f"\n\nхочешь: "),
        data.get("wishlist"),
        italic(f"\n\nне хочешь: "),
        data.get("hatelist")
    ) 
    await call.message.answer_photo(photo=data.get("photo_url"), caption=message,
        reply_markup=hub_keyboard)


