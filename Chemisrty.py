from tkinter import *
import re


def window_open(label_1):  # Всплывающее окно

    toplevel = Toplevel()
    toplevel.title("Химический элемент таблицы Менделеева")
    toplevel.geometry("700x500+600+200")

    label = Label(toplevel, text='Порядковый номер элемента', height=0, width=600, wraplength=700)
    label.pack()
    scroll = Scrollbar(toplevel, orient='vertical')
    scroll.pack(side=RIGHT, fill=Y)

    text = Text(toplevel)
    text.insert(END, label_1 * 5)
    text.configure(yscrollcommand=scroll.set)
    text.pack(side=LEFT, fill=BOTH)



def output(event):  # Обработка вводимого текста и неправильного ввода

    txt = entry1.get()
    try:
        if txt.isnumeric():
            n = int(txt)
            if n > 0:
                if int(txt) > 0:
                    chem_element_numer(int(txt))
                elif int(txt) <= 0:
                    window_open("Введите положительный номер элемента")
        else:
            chem_element_word(txt)
    except ValueError:
        window_open("Введите корректный номер элемента")

def chem_element_word(word):  # Поиск текста в текстовом файле по названию \d\:{}: \[([^\[\]]+)\]

    text = "chemistry_elements.txt"
    element_file = open(text, mode='r')
    look_text = element_file.read()
    number = word.lower()
    textsearch = r"\d\:{}: \[([^\[\]]+)\]".format(number)
    result = re.findall(textsearch, look_text)

    return window_open(result)

def chem_element_numer(num):  # Поиск текста в текстовом файле по номеру {}:.+: \[([^\[\]]+)\]

    text = "chemistry_elements.txt"
    element_file = open(text, mode='r')
    look_text = element_file.read()
    number = num
    textsearch = r"{}:.+: \[([^\[\]]+)\]".format(number)
    result = re.findall(textsearch, look_text)

    return window_open(result)


app = Tk()
app.title("Химические элементы таблицы Менделеева")
app.geometry("500x150+600+400")

label = Label(app, text="Введите номер химического элемента", height=0, width=100)
label.pack()

b = Button(app, text="Выход", width=0, command=app.destroy)
b.pack(side='bottom', padx=0, pady=0)

button1 = Button(app, text="Введите порядковый номер или название элемента", width=0)
button1.pack(side='bottom', padx=5, pady=5)
button1.bind("<Button-1>", output)

entry1 = Entry(app, width=26, font=3)
entry1.pack(side='bottom', padx=5, pady=5)


app.mainloop()