from datetime import datetime
from dpfuncs import date_format

class Person:

    def __init__(self, fname, mname, lname, dbirth, ddeath, sex):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.dbirth = dbirth
        self.ddeath = ddeath
        self.sex = sex

    def __str__(self):
        # Обчислення віку людини -> повних років.
        age = str(self.calculate_age())

        # Перевірка віку людини для визначення необхідного слова "рік", "років" або "роки".
        if age[-1] == "1" and len(age) == 1 or age[-1] == "1" and age[-2] != "1":
            years = "рік"
        elif age[-1] in "234" and len(age) == 1 or age[-1] in "234" and age[-2] != "1":
            years = 'роки'
        else:
            years = 'років'

        # Перевірка введеного значення статі
        # для визначення необхідних слів для статті людини.
        if self.sex in 'mчм':
            sex, born, died = 'чоловік', 'Народився', 'Помер'
        elif self.sex in 'fwж':
            sex, born, died = 'жінка', 'Народилася', 'Померла'
        else:
            sex, born, died = 'невідомої статі', 'Народилося', 'Померло'

        # Формування списку з усіх даних,
        # які потрібні для відображення інформації про людину
        strng = [f'{self.lname}',
                 f'{self.fname}',
                 f'{self.mname}',
                 f'{age}',
                 f'{years},',
                 f'{sex}.',
                 f'{born}:',
                 f'{self.dbirth}.',
                 f'{died}:',
                 f'{self.ddeath}.']

        # Вилучення зі списку даних, які не були введені користувачем
        strng = list(filter(lambda x: x, strng))

        # Формування строки для відображення користувачу інформації про особу
        return ' '.join(strng) if self.ddeath else ' '.join(strng[:-2])


    def calculate_age(self):

        # Переведення дат str -> datetime та визначення останнього дня життя для визначення віку
        birthday = date_format(self.dbirth)
        lastday = date_format(self.ddeath) if self.ddeath else datetime.today()

        # Обчислення різниці років в датах
        age = lastday.year - birthday.year

        # Проведення перевірки місяця та дня народження для визначення повних років
        if lastday.month < birthday.month or lastday.month == birthday.month and lastday.day < birthday.day:
            age -= 1

        return age
