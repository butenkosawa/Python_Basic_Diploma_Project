from datetime import datetime


def date_format(date: str) -> datetime:
    """Перетворює дату зі строки у формат дати.

    :param date: дата у форматі dd.mm.yyyy -> str
    :return: дата у форматі yyyy-mm-dd hh:mm:ss -> datetime
    """

    return datetime.strptime(date, "%d.%m.%Y")


def if_date_format(date: str) -> str:
    """Перетворює дату введену користувачем у формат dd.mm.yyyy,
    або повертає строку "Invalid date format".

    :param date: дата у одному з форматів dd.mm.yyyy, dd/mm/yyyy, dd-mm-yyyy, dd mm yyyy, yyyy-dd-mm -> str
    :return: дата у форматі dd.mm.yyyy, або строка "Invalid date format" -> str
    """

    if not date:
        return ""

    date = ''.join(map(lambda x: x if x.isdigit() else ".", date))

    try:
        date = date_format(date)
        return date.strftime("%d.%m.%Y")
    except ValueError:
        return "Invalid date format"


def check_date_format(date: str) -> str:
    """Перевіряє в циклі введену користувачем дату, яка повинна відповідати
    визначеним форматам доки не буде введено коректну дату

    :param date: дата у форматі dd.mm.yyyy -> str
    :return: дата у форматі dd.mm.yyyy -> str
    """

    while date == "Invalid date format":
        print('Невірний формат дати.')
        date = if_date_format(input('Ведіть дату у форматі ДД.ММ.РРРР: '))

    return date


def check_deathdate(birthdate: str, deathdate: str) -> str:
    """Перевіряє чи введена користувачем дата смерті не раніше дати нарадження

    :param birthdate: введена користувачем дата народження: str
    :param deathdate: введена користувачем дата смерті: str
    :return: дата смерті: str
    """

    birthdate = datetime.strptime(birthdate, "%d.%m.%Y")
    deathdate = datetime.strptime(deathdate, "%d.%m.%Y")

    while deathdate < birthdate:
        print('Дата смерті раніше за дату народження.')
        deathdate = if_date_format(input('Ведіть коректну дату: '))
        deathdate = check_date_format(deathdate)
        deathdate = datetime.strptime(deathdate, "%d.%m.%Y")

    return deathdate.strftime("%d.%m.%Y")


def mandatory_attr(attr: str) -> str:
    """Перевіряє обов'язкове введення даних в поле користувачем"""

    while not attr:
        attr = input('Це поле обов’язкове. Введіть дані: ')
    return attr


def mandatory_date(date):
    """Перевіряє обов'язкове введення дати в поле користувачем"""

    while not date:
        date = if_date_format(input('Це поле обов’язкове. Введіть дані: '))
    return date
