from bot import dp, bot, UserState
from aiogram.utils.markdown import text, bold
from aiogram.types import Message, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

from src.helpers.delete_messages import delete_messages_for_count

@dp.message_handler(content_types=["text"], state=UserState.Registration.WatingName)
async def on_register_get_name_handler(message: Message, state: FSMContext):
    await delete_messages_for_count(message, bot)
    name = message.text.strip() 
    await state.update_data(name=name)
    await message.answer(
        text(
            f"Добро пожаловать {name}",
            "\n\n Отправль фоточку, которую увидит твой санта (только одну плиз)📷"
            )
    )
    await UserState.Registration.next()

@dp.message_handler(content_types=["photo"], state=UserState.Registration.WatingPhoto)
async def on_register_get_photo_handler(message: Message, state: FSMContext):
    await delete_messages_for_count(message, bot)
    photo_url = message.photo[-1].file_id
    await state.update_data(photo_url=photo_url)
    await message.answer_photo(
        photo=photo_url,
        caption=text(
            "Отлично... ну ты конечно -> 🤡(клоун)",
            "\nНо все равно красивый!🧑🏻‍🎄",
            "\nТеперь мне нужно что бы ты сказал свои хотелки и пожелания"
            "\n\nчто бы твой санта мог выбрать тебе лучщий подарок!!",
            "\n\n И не забывай что у нас бюджет от 1500 до 2000 рублей (что бы никого не разорять)",
            "\nИ отправль все одиним сообщением!!!"
        ))
    await UserState.Registration.next()

@dp.message_handler(content_types=["text"], state=UserState.Registration.WatingWishlist)
async def on_register_get_wishlist_handler(message: Message, state: FSMContext):
    await delete_messages_for_count(message, bot)
    await state.update_data(wishlist=message.text)
    await message.answer(
        text(
            "Ну у тебя и пожелания...",
            bold("\nно не волнуйся\\!!!"),
            "\nя все передм твоему санте в точности до буквы\\!",
            bold("\n\nТеперь расскажи чего бы тебе точно не хотелось🛑")
            )
        )
    await UserState.Registration.next()

@dp.message_handler(content_types=["text"], state=UserState.Registration.WatingHateList)
async def on_register_get_hatelist_handler(message: Message, state: FSMContext):
    await delete_messages_for_count(message, bot)
    await state.update_data(hatelist=message.text)
    await message.answer(
        text(
            "ну ты и душнила... 🤡",
            bold("\nно не волнуйся\\!!!"),
            "\nя все передм твоему санте в точности до буквы\\!",
            "\nтыкни на кнопку внизу пожалуйста"
            ),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Нажми✅", callback_data="hub")]]
))
    await UserState.Hub.Main.set()