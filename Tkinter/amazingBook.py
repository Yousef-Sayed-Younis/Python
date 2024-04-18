from tkinter import *
from tkinter import ttk

f = Tk()
f.title("Test")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 30)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)

options = ["Computer", "Music", "Media", "Arts", "Home Economy"]


def show():
    lb.config(text=clicked.get())


ttk.Label(f, text="Your department is").pack()

clicked = StringVar()
clicked.set("Media")

lbx = ttk.OptionMenu(f, clicked, *options)
lbx.pack()


ttk.Button(f, text="Click me", command=show).pack()

lb = ttk.Label(f, text="")
lb.pack()

f.mainloop()
