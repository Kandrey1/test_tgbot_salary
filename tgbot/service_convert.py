import datetime
import ast


class Convert:
    """
    Содержит методы для преобразования данных.
    """
    @classmethod
    async def str_in_datetime(cls, string: str) -> datetime:
        """
            Преобразует строку формата ISO в объект datetime
            :param
                string: строка в формате ISO.
        """
        return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%S")

    @classmethod
    async def datetime_in_str(cls, date: datetime) -> str:
        """
        Преобразует объект datetime в строку формата ISO.
        :param
            string: строка в формате ISO.
        """
        return date.strftime("%Y-%m-%dT%H:%M:%S")

    @classmethod
    async def list_in_dict(cls, data: list[dict]) -> dict:
        """
        Преобразует список словарей(дата-время, сумма) в словарь с
        ключом дата-время и значением сумма.

        :param
            data: список словарей(дата-время, сумма)
        :return:
            словарь с ключом дата-время и значением сумма.
        """
        return {d['_id']: d['total'] for d in data}

    @classmethod
    async def input_str_to_dict(cls, string: str) -> dict:
        """
        Преобразует строку пользователя в словарь для запроса.

        :param
            string: строка из сообщения.
        :return:
            словарь запроса.
        """
        return ast.literal_eval(string)
