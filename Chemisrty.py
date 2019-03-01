from tkinter import *
import re

def output(event):
    txt = entry1.get()


    text = "chemistry_elements.txt"
    element_file = open(text, mode='r')
    look_text = element_file.read()
    num = txt
    textsearch = r"{}:\[(.+)\]".format(num)

    result = re.findall(textsearch, look_text)

    toplevel = Toplevel()
    label1 = Label(toplevel, text=result, height=0, width=100, wraplength=700)
    label1.pack()


app = Tk()
app.title("Химические элементы таблицы Менделеева")
app.geometry("500x150+200+200")



label = Label(app, text="Введите номер химического элемента", height=0, width=100)
b = Button(app, text="Выход", width=20, command=app.destroy)
button1 = Button(app, text="Введите порядковый номер", width=30)
entry1 = Entry(app, width=3, font=3)


label.pack()
b.pack(side='bottom',padx=0,pady=0)
button1.pack(side='bottom',padx=5,pady=5)
entry1.pack(side='bottom',padx=5,pady=5)

button1.bind("<Button-1>", output)

app.mainloop()