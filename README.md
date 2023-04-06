# Тестовое задание.

Описание задачи:
Вашей задачей в рамках этого тестового задания будет написание
алгоритма агрегации статистических данных о зарплатах
сотрудников компании по временным промежуткам. Ссылка на
скачивание коллекции со статистическими данными, которую
необходимо использовать при выполнении задания, находится в
конце документа.
На обычном языке пример задачи выглядит следующим образом:
“Необходимо посчитать суммы всех выплат с 28.02.2022 по
31.03.2022, единица группировки - день”.
Ваш алгоритм должен принимать на вход:
1. Дату и время старта агрегации в ISO формате (далее dt_from)
2. Дату и время окончания агрегации в ISO формате (далее
dt_upto)
3. Тип агрегации (далее group_type). Типы агрегации могут быть
следующие: hour, day, month. То есть группировка всех данных
за час, день, неделю, месяц.
Пример входных данных:

{"
dt_from":"2022-09-01T00:00:00",
"dt_upto":"2022-12-31T23:59:00",
"group_type":"month"
}

Комментарий к входным данным: вам необходимо агрегировать
выплаты с 1 сентября 2022 года по 31 декабря 2022 года, тип
агрегации по месяцуНа выходе ваш алгоритм формирует ответ
содержащий:
4. Агрегированный массив данных (далее dataset)
5. Подписи к значениям агрегированного массива данных в ISO
формате (далее labels)
Пример ответа:
 
{"dataset": [5906586, 5515874, 5889803, 6092634], "labels":
["2022-09-01T00:00:00", "2022-10-01T00:00:00",
"2022-11-01T00:00:00", "2022-12-01T00:00:00"]}

Комментарий к ответу: в нулевом элементе датасета содержится
сумма всех выплат за сентябрь, в первом элементе сумма всех
выплат за октябрь и т.д. В лейблах подписи соответственно
элементам датасета.


## Установка и запуск
Выполнить следующие команды:

- Клонировать репозиторий: `git clone https://github.com/Kandrey1/test_tgbot_salary.git`

- Создать виртуальное окружение командой: `python -m venv venv`

- Установить пакеты: `pip install -r requirements.txt`

- Создать и заполнить файл .env по примеру .env.example

- У Вас должнa быть установлена база данных MongoDb на порту 27017. Если она на 
другом порте тогда в файле config.py установить нужный порт `MONGODB_PORT = `


- Для запуска приложения выполнить команду `python run_bot.py`
