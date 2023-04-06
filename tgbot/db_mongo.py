from pymongo import MongoClient

from config import Settings
from .service_convert import Convert

client = MongoClient(Settings.MONGODB_HOST, Settings.MONGODB_PORT)

db = client['sampleDB']


async def aggregation_salary(request: dict) -> list[dict]:
    """
    Агрегации статистических данных о зарплатах сотрудников компании
    по временным промежуткам.

    :param:
        request: словарь содержащий дату и время старта агрегации в ISO формате,
              дату и время окончания агрегации в ISO формате и тип агрегации.

    :return:
        Возвращает список из словарей содержащих дату-время и сумму.
    """
    date_format = {
        'year': {"$year": "$dt"},
        'month': {"$month": "$dt"},
        'day': {"$dayOfMonth": "$dt"} if request['group_type'] in ['hour', 'day'] else 1,
        'hour': {"$hour": "$dt"} if request['group_type'] == 'hour' else 0,
    }

    start = await Convert.str_in_datetime(request['dt_from'])
    end = await Convert.str_in_datetime(request['dt_upto'])

    cursor = db.sample_collection.aggregate([
        {"$match": {"dt": {"$gte": start, "$lte": end}}},
        {"$project": {
            "value": 1,
            "label": {
                "$dateFromParts": {
                    'year': date_format['year'],
                    'month': date_format['month'],
                    'day': date_format['day'],
                    'hour': date_format['hour'],
                    'minute': 0,
                    'second': 0,
                }
            },
        }},
        {"$group": {
            "_id": "$label",
            "total": {"$sum": "$value"}
        }},
        {"$sort": {"_id": 1}}
    ])

    return list(cursor)
