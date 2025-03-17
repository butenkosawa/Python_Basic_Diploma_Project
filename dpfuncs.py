from datetime import datetime


def date_format(date):
    return datetime.strptime(date, "%d.%m.%Y")


def if_date_format(date):
    possible_formats = [
        "%d.%m.%Y",
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%d %m %Y",
        "%Y-%m-%d"
    ]

    if not date:
        return None

    for fmt in possible_formats:
        try:
            parsed_date = datetime.strptime(date, fmt)
            return parsed_date.strftime("%d.%m.%Y")
        except ValueError:
            continue

    return "Invalid date format"


def check_date_format(date):
    while date == "Invalid date format":
        print('Невірний формат дати.')
        date = if_date_format(input('Ведіть дату у форматі ДД.ММ.РРРР: '))
    return date


def check_deathdate(birthdate, deathdate):
    birthdate = datetime.strptime(birthdate, "%d.%m.%Y")
    deathdate = datetime.strptime(deathdate, "%d.%m.%Y")
    while deathdate < birthdate:
        print('Дата смерті раніше за дату народження.')
        deathdate = if_date_format(input('Ведіть коректну дату: '))
        deathdate = check_date_format(deathdate)
        deathdate = datetime.strptime(deathdate, "%d.%m.%Y")
    return deathdate.strftime("%d.%m.%Y")


def mandatory_attr(attr):
    while not attr:
        attr = input('Це поле обов’язкове. Введіть дані: ')
    return attr


def mandatory_date(date):
    while not date:
        date = if_date_format(input('Це поле обов’язкове. Введіть дані: '))
    return date


def infinite_sequence(start):
    num = start
    while True:
        yield num
        num += 1
