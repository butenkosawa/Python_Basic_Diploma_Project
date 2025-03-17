import json
from person import Person
from dpfuncs import *

print('ДАНІ ПРО ЛЮДЕЙ'.center(33, '-'))
persons = []

while True:
    print('\n' + 'Меню'.center(33, '-'))
    print('1. Внести дані')
    print('2. Переглянути дані')
    print('3. Завантажити дані з файлу')
    print('4. Зберегти дані у файл')
    print('5. Вихід')
    choice = input('\nВиберіть необхідний пункт меню: ')

    if choice in '12345':

        if choice == '1':
            print("\nПоля, помічені '*' обов’язкові для введення даних!")

            lname = input('Прізвище: ').upper()

            fname = input('* Ім’я *: ').title()
            fname = mandatory_attr(fname).title()

            mname = input('По батькові: ').title()

            sex = input('* Стать *: ').lower()
            sex = mandatory_attr(sex).lower()

            dbirth = if_date_format(input('* Дата народження *: '))
            dbirth = mandatory_date(dbirth)
            dbirth = check_date_format(dbirth)

            ddeath = if_date_format(input('Дата смерті: '))
            ddeath = check_date_format(ddeath)
            if ddeath:
                ddeath = check_deathdate(dbirth, ddeath)

            persons.append(Person(fname, mname, lname, dbirth, ddeath, sex[0]))


        elif choice == '2':

            while True:
                print('\n' + 'Оберіть параметри перегляду'.center(33, '-'))
                print('1. Переглянути дані про всіх осіб')
                print('2. Пошук даних за іменем')
                print('3. Повернутися до попереднього меню')
                choice2 = input('\nВиберіть необхідний пункт меню: ')

                if choice2 in '123':

                    if choice2 == '1':
                        if len(persons) == 0:
                            print('Даних про людей не знайдено.')
                        else:
                            for person in persons:
                                print(person)

                    if choice2 == '2':
                        searched_person = input('Пошук: ').lower()
                        search_result = []

                        for person in persons:
                            if searched_person in str(person).lower():
                                search_result.append(person)

                        if len(search_result) == 0:
                            print('Особу не знайдено.')
                        else:
                            for person in search_result:
                                print(person)

                    if choice2 == '3':
                        break

                else:
                    print('Такого пункту меню не існує!')


        elif choice == '3':
            file_name = input('Введіть назву файлу, з якого необхідно завантажити дані: ') + '.json'

            with open(file_name, 'r', encoding='utf-8') as file:
                loaded_data = json.load(file)

            for person in loaded_data:
                persons.append(Person(
                    person['fname'],
                    person['mname'],
                    person['lname'],
                    person['dbirth'],
                    person['ddeath'],
                    person['sex']
                ))


        elif choice == '4':
            file_name = input('Введіть назву файлу: ') + '.json'

            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump([person.__dict__ for person in persons], file, indent=4, ensure_ascii=False)


        else:
            break

    else:
        print('Такого пункту меню не існує!')
