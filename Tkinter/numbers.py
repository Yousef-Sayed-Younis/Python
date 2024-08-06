import tkinter
import tkinter as tk
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

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def printNUM():
    ttk.Label(f, text=lbx.get(ACTIVE)).place(x=480, y=200)


lbx = Listbox(f, justify=CENTER, height=23, selectmode="multiple")

for i in range(1, 101):
    lbx.insert(i, i)

scr = ttk.Scrollbar(f, command=lbx.yview)
scr.pack(side=RIGHT, fill=Y)

lbx.configure(
    background="lightblue", foreground="green", yscrollcommand=scr.set
)

lbx.pack(anchor=CENTER)


ttk.Button(f, text="Print Selected", width=20, command=printNUM).pack()

f.mainloop()
