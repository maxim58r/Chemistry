from tkinter import *
import re


def window_open(label_1):  # Всплывающее окно
    toplevel = Toplevel()
    label_new = Label(toplevel, text=label_1, height = 0, width = 100, wraplength = 700)
    label_new.pack()

def output(event):  # Обработка вводимого текста и неправильного ввода

    txt = entry1.get()
    try:
        if int(txt) > 0:
            chem_element_numer(int(txt))
        else:
            window_open("Введите положительный номер элемента")
    except ValueError:
        window_open("Введите корректный номер элемента")

def chem_element_word(word):  # Поиск текста в текстовом файле по названию

    text = "text.txt"
    element_file = open(text, mode='r')
    look_text = element_file.read()
    number = word
    textsearch = r"\d\:\{}:".format(number)
    result = re.findall(textsearch, look_text)

    return window_open(result)

def chem_element_numer(num):  # Поиск текста в текстовом файле по номеру

    text = "text.txt"
    element_file = open(text, mode='r')
    look_text = element_file.read()
    number = num
    textsearch = r"{}:\[(.+)\]".format(number)
    result = re.findall(textsearch, look_text)

    return window_open(result)


app = Tk()
app.title("Химические элементы таблицы Менделеева")
app.geometry("500x150+200+200")

label = Label(app, text="Введите номер химического элемента", height=0, width=100)
label.pack()

b = Button(app, text="Выход", width=20, command=app.destroy)
b.pack(side='bottom', padx=0, pady=0)

button1 = Button(app, text="Введите порядковый номер", width=30)
button1.pack(side='bottom', padx=5, pady=5)
button1.bind("<Button-1>", output)

entry1 = Entry(app, width=3, font=3)
entry1.pack(side='bottom', padx=5, pady=5)


app.mainloop()