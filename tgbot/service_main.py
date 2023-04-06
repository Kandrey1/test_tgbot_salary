import datetime
import json

from .service_convert import Convert
from .db_mongo import aggregation_salary


async def generate_labels(data: dict):
    """
    Генерирует список (временного промежутка)
    :param
        data: словарь с датой начала, окончания и типом группировки.
    :return:
        Список с датами.
    """
    dct = {
        'month': datetime.timedelta(days=31),
        'day': datetime.timedelta(days=1),
        'hour': datetime.timedelta(hours=1)
    }

    start_date = await Convert.str_in_datetime(data['dt_from'])
    end_date = await Convert.str_in_datetime(data['dt_upto'])

    delta = dct[data['group_type']]

    labels = list()
    while start_date <= end_date:
        # Для месяца. Если дельта устанавливает дату не на 1 число,
        # принудительно ставится 1 число.
        if data['group_type'] == 'month' and start_date.day >= 2:
            start_date = start_date.replace(day=1)

        labels.append(start_date)
        start_date += delta

    return labels


async def get_salaries(request: dict) -> json:
    """
    Возвращает словарь с dataset и labels.
    :param
        request: запрос(словарь) содержащий дату старта и окончания
                 агрегации, а также тип группировки.
    """
    output = dict()
    output['dataset'] = list()
    output['labels'] = list()

    response = await aggregation_salary(request)
    dct_salary = await Convert.list_in_dict(response)

    labels = await generate_labels(request)

    for item in labels:
        output["labels"].append(await Convert.datetime_in_str(item))
        if dct_salary.get(item, None):
            output["dataset"].append(dct_salary[item])
        else:
            output["dataset"].append(0)

    return json.dumps(output)
