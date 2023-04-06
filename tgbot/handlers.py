from aiogram import types, Dispatcher

from .service_main import get_salaries
from .service_convert import Convert


async def cmd_start(message: types.Message):
    """
    Старт раздела: Интересные ссылки.
    """
    await message.reply(f"Hi,{message.from_user.username} ")


async def cmd_all_msg(message: types.Message):
    """
    Обрабатывает запрос
    """
    # Преобразование строки в словарь запроса.
    try:
        request = await Convert.input_str_to_dict(message.text)

        # Ответ на запрос.
        response = await get_salaries(request)
        await message.answer(str(response))

    except Exception:
        await message.answer('Невалидный запрос. Пример запроса:\n'
                             '{"dt_from": "2022-09-01T00:00:00",\n'
                             '"dt_upto": "2022-12-31T23:59:00",\n'
                             '"group_type": "month"}')


def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")

    dp.register_message_handler(cmd_all_msg)
