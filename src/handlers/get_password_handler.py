from bot import dp, bot, UserState
from aiogram.utils.markdown import text, bold
from aiogram.types import Message, ParseMode
from aiogram.dispatcher import FSMContext

from config import PASSWORD

from src.helpers.delete_messages import delete_messages_for_count

@dp.message_handler(content_types=["text"] ,state=UserState.Registration.WatingPassword)
async def get_password_handler(message: Message, state: FSMContext):
    await delete_messages_for_count(message, bot)
    if message.text.strip() == PASSWORD:
        await message.answer(
            text(
                bold("УРААА, добро пожаловать... пока хз кто ты❔"),
                "\n\nно я очень рад что ты тоже решил к нас присоедениться\\!",
                bold("\n\nУКАЖИ СВОЙ ИНДИФИКАТОР\\(ИМЯ\\)\n"),
                "\nно только так что бы поняли другие додики\\.\\.\\.🧘🏻"
                ),
            parse_mode=ParseMode.MARKDOWN_V2
        )
        await UserState.Registration.next()
    else:
        await message.answer(
            "No. Уходи Джъагель 💩💩💩"
        )
        await state.finish()
    
