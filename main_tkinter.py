import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from dpfuncs import date_format, if_date_format
from person import Person


persons = []


def input_data():
    lname = entry1.get().upper()
    fname = entry2.get().title()
    mname = entry3.get().title()
    dbirth = if_date_format(entry4.get())
    ddeath = if_date_format(entry5.get())
    sex = combo.get().lower()

    try:
        assert all([fname, dbirth]), \
            'Будь ласка, введіть Ім’я та Дату народження.'
        assert dbirth != 'Invalid date format' and ddeath != 'Invalid date format', \
            'Будь ласка, введіть дату у форматі ДД.ММ.РРРР'
        if ddeath:
            assert date_format(ddeath) > date_format(dbirth), \
                'Дата смерті раніше за дату народження.'

        persons.append(Person(fname, mname, lname, dbirth, ddeath, sex[0]))
        show_info(persons)

        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)


    except AssertionError as msg:
        messagebox.showinfo('Помилка', msg)


def search_person():
    searched_person = entry6.get().lower()
    search_result = []

    for person in persons:
        if searched_person in str(person).lower():
            search_result.append(person)

    if len(search_result) == 0:
        text_out.delete(1.0, tk.END)
        text_out.insert(tk.END, 'Особу не знайдено.\n')
    else:
        show_info(search_result)
        entry6.delete(0, tk.END)


def open_file():
    global persons
    file_name = askopenfilename(defaultextension='.json',
                                filetypes=[('JSON files', '*.json'),
                                           ('Python files', '*.py'),
                                           ('All files', '*.*')]
                                )

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

    persons = list({str(person): person for person in persons}.values())
    show_info(persons)


def save_file():
    file_name = asksaveasfilename(defaultextension='.json',
                                  filetypes=[('JSON files', '*.json'),
                                             ('Python files', '*.py'),
                                             ('All files', '*.*')]
                                  )
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump([person.__dict__ for person in persons], file, indent=4, ensure_ascii=False)


def display_info():
    show_info(persons)


def clean_text():
    text_out.delete(1.0, tk.END)


def clean_data():
    global persons
    persons = []


def about_project():
    with open('Diplom Task.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    text_out.delete(1.0, tk.END)
    text_out.insert(tk.END, data)


def show_info(people: list):
    text = ''
    for person in people:
        text += str(person) + '\n'
    text_out.delete(1.0, tk.END)
    text_out.insert(tk.END, text)


root = tk.Tk()
root.title('    Дані про людей')
root.iconbitmap('icon.ico')
root.resizable(False, False)
root.configure(padx=10, pady=10, bg='#9EB3C2')

label1 = tk.Label(root, text='Прізвище')
label2 = tk.Label(root, text='Ім’я')
label3 = tk.Label(root, text='По батькові')
label4 = tk.Label(root, text='Дата народження')
label5 = tk.Label(root, text='Дата смерті')
label6 = tk.Label(root, text='Стать')

label1.grid(row=0, column=0, sticky='e', padx=5, pady=10)
label2.grid(row=1, column=0, sticky='e', padx=5, pady=10)
label3.grid(row=2, column=0, sticky='e', padx=5, pady=10)
label4.grid(row=0, column=2, sticky='e', padx=5, pady=10)
label5.grid(row=1, column=2, sticky='e', padx=5, pady=10)
label6.grid(row=2, column=2, sticky='e', padx=5, pady=10)

label1.configure(bg='#9EB3C2', fg='#01161E', font=('Tahoma', 10, 'bold'))
label2.configure(bg='#9EB3C2', fg='#01161E', font=('Tahoma', 10, 'bold'))
label3.configure(bg='#9EB3C2', fg='#01161E', font=('Tahoma', 10, 'bold'))
label4.configure(bg='#9EB3C2', fg='#01161E', font=('Tahoma', 10, 'bold'))
label5.configure(bg='#9EB3C2', fg='#01161E', font=('Tahoma', 10, 'bold'))
label6.configure(bg='#9EB3C2', fg='#01161E', font=('Tahoma', 10, 'bold'))

entry1 = tk.Entry(root, bg='#E0E3DD', fg='#01161E', font=('Arial', 10))
entry2 = tk.Entry(root, bg='#E0E3DD', fg='#01161E', font=('Arial', 10))
entry3 = tk.Entry(root, bg='#E0E3DD', fg='#01161E', font=('Arial', 10))
entry4 = tk.Entry(root, bg='#E0E3DD', fg='#01161E', font=('Arial', 10))
entry5 = tk.Entry(root, bg='#E0E3DD', fg='#01161E', font=('Arial', 10))
entry6 = tk.Entry(root, bg='#E0E3DD', fg='#01161E', font=('Arial', 10))

entry1.grid(row=0, column=1, padx=5, pady=10)
entry2.grid(row=1, column=1, padx=5, pady=10)
entry3.grid(row=2, column=1, padx=5, pady=10)
entry4.grid(row=0, column=3, padx=5, pady=10)
entry5.grid(row=1, column=3, padx=5, pady=10)
entry6.grid(row=0, column=4, padx=5, pady=10)

button1 = tk.Button(root, text='Пошук', command=search_person)
button2 = tk.Button(root, text='Ввести', command=input_data)

button1.grid(row=1, column=4, padx=5, pady=10)
button2.grid(row=2, column=4, padx=5, pady=10)

button1.configure(width=15, bg='#B8BFB0', font=('Arial', 9))
button2.configure(width=15, bg='#B8BFB0', font=('Arial', 9))

combo = ttk.Combobox(root, values=('Чоловік', 'Жінка'))
combo.current(0)
combo.configure(background='#E0E3DD')
combo.grid(row=2, column=3)

text_out = tk.Text(root, height=15, width=100, bg='#E5EBEA', fg='#01161E', font=('Arial', 10))
text_out.grid(row=3, column=0, columnspan=6)

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar)
menubar.add_cascade(label='Файл', menu=filemenu)
filemenu.add_command(label='Відкрити', command=open_file)
filemenu.add_command(label='Зберегти', command=save_file)

actionmenu = tk.Menu(menubar)
menubar.add_cascade(label='Дія', menu=actionmenu)
actionmenu.add_command(label='Відобразити', command=display_info)
actionmenu.add_command(label='Очистити текст', command=clean_text)
actionmenu.add_command(label='Очистити дані', command=clean_data)

helpmenu = tk.Menu(menubar)
menubar.add_cascade(label='Допомога', menu=helpmenu)
helpmenu.add_command(label='Про програму', command=about_project)

root.config(menu=menubar)

root.mainloop()
