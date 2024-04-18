from re import L
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


def remain():
    Label(f, text=int(n1.get()) % int(n2.get())).pack()


def power():
    Label(f, text=int(n1.get()) ** int(n2.get())).pack()


n1 = Entry(f, width=20)
n2 = Entry(f, width=20)

n1.pack()
n2.pack()

Button(f, text="N1%N2", width=20, command=remain).pack()

Button(f, text="N1^N2", width=20, command=power).pack()

f.mainloop()
