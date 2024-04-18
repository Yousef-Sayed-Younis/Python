import tkinter
from tkinter import ttk
from tkinter import *


f = tkinter.Tk()
f.title("Choose")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def add():
    n = 0
    lbx.insert(n, ent.get())
    n += 1


lbx = Listbox(f)
lbx.grid(column=2, row=0)

ent = ttk.Entry(f, width=20)
ent.grid(column=2, row=1)

ttk.Button(f, text="Add item", command=add).grid(column=2, row=2)

f.mainloop()
