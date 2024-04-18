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

options = ["Computer", "Music", "Media", "Arts", "Home Economy"]


def show():
    lb.config(text=f"Department is {clicked.get()}")


ttk.Label(f, text="Your department is").grid(column=0, row=0, ipadx=20)

clicked = StringVar()
clicked.set("Media")

lbx = OptionMenu(f, clicked, *options)
lbx.grid(column=1, row=0)


Button(f, text="Click me", command=show).grid(column=1, row=1)

lb = Label(f, text=" ")
lb.grid(column=1, row=2)

f.mainloop()
