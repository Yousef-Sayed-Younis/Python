import tkinter
from tkinter import *
from tkinter import ttk

f = tkinter.Tk()
f.title("Best Doctor")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def chData():
    ent.delete(0, END)
    ent.insert(0, "Dr.Hend")


ttk.Label(f, text="Best Doctor is").pack()


ent = ttk.Entry(f, width=20)
ent.insert(0, "nodata")
ent.pack()

Button(f, text="Click", command=chData).pack()

f.mainloop()
