import tkinter
from tkinter import *
from tkinter import ttk


f = tkinter.Tk()
f.title("Test")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def even():
    text = int(en.get())
    Label(f, text="Even Number" if text % 2 == 0 else "Odd Number").pack()


en = Entry(f)

en.pack()

Button(f, text="Show Even", width=20, command=even).pack()

f.mainloop()
