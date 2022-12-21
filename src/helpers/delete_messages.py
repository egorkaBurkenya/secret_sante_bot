from aiogram.types import Message
from aiogram import Bot

async def delete_messages_for_count(message: Message, bot: Bot, count: int = 2) -> None:
    if count == 2:
        await message.delete()
        await bot.delete_message(
            chat_id = message["chat"]["id"], 
            message_id = message["message_id"] - 1
            )
    else:
        print("Пока не работает")
