from tkinter import *

ABOUT_TEXT = """"Водоро́д (H, лат. hydrogenium) 
 1-й химический элемент периодической системы. Самый
  распространённый во Вселенной элемент. Как простое
  вещество — H2 — представляет собой лёгкий бесцветный
  газ, который в смеси с воздухом или кислородом горюч и взрывоопасен!"
"""



def clickAbout():
    toplevel = Toplevel()
    label1 = Label(toplevel, text=ABOUT_TEXT, height=0, width=100)
    label1.pack()
    #label2 = Label(toplevel, text=DISCLAIMER, height=0, width=100)
    #label2.pack()


app = Tk()
app.title("SPIES")
app.geometry("500x300+200+200")

label = Label(app, text="Введите номер химического элемента", height=0, width=100)
b = Button(app, text="Quit", width=20, command=app.destroy)
button1 = Button(app, text="About SPIES", width=20, command=clickAbout)

label.pack()
b.pack(side='bottom',padx=0,pady=0)
button1.pack(side='bottom',padx=5,pady=5)

app.mainloop()