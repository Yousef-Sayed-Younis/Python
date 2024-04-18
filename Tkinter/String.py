import tkinter
from tkinter import *
from tkinter import ttk


f = tkinter.Tk()
f.title("Print Number")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(
    style='TLabel', font=fnt, background='lightblue', foreground='green',
)

ttk.Style().configure(
    style="TEntry", width=4, font=fnt,
)


def showLength():
    Label(f, text=len(en.get())).pack()


def cap():
    text = en.get().upper()
    en.delete(0, "end")
    en.insert(0, text)


def capFirst():
    text = en.get().capitalize()
    en.delete(0, "end")
    en.insert(0, text)


def swapCase():
    text = en.get().swapcase()
    en.delete(0, "end")
    en.insert(0, text)


def reverse():
    text = en.get()[::-1]
    en.delete(0, "end")
    en.insert(0, text)


en = Entry(f)
en.pack()

Button(f, text="Show Length", width=20, command=showLength).pack()

Button(f, text="Capitalize", width=20, command=cap).pack()

Button(f, text="Capitalize First", width=20, command=capFirst).pack()

Button(f, text="Swap Case", width=20, command=swapCase).pack()

Button(f, text="Reverse", width=20, command=reverse).pack()

f.mainloop()
