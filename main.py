from os import environ
from asyncio import get_event_loop
from logging import basicConfig, INFO

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

import sys

from handlers import start, channels

dp = Dispatcher()

channel_id = -1001544003532
load_dotenv()

'''@dp.message()
async def start_command(message: Message, bot: Bot):
    await bot.send_message(chat_id = channel_id, text="Test text from python!")
    return await message.reply("Да!")'''

async def main():
    print(sys.argv)
    bot = Bot(sys.argv[1])
    dp.include_routers(start.router, channels.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await bot.send_message(text="Test text from python!")


if __name__ == '__main__':
    basicConfig(level=INFO)
    loop = get_event_loop()
    loop.run_until_complete(main())



from .. import text
print(text.a)
