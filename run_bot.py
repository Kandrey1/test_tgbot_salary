import logging
from aiogram.utils import executor
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from config import Settings
from tgbot.handlers import register_handlers_main

bot = Bot(token=Settings.TG_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


# Записывает в лог сообщение о старте бота.
async def on_startup(_) -> None:
    logging.info('Бот запущен')


# Записывает в лог сообщение о завершении работы бота.
async def on_shutdown(_) -> None:
    logging.info('Бот остановлен')


# Регистрация хэндлеров.
register_handlers_main(dp)


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
