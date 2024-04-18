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


def submit():
    with open("FormInfo.txt", "w") as f:
        for i in entry:
            f.write(i.get() + "\n")


entry = []
info = ["ID", "Name", "Date", "Address", "Phone NO.", "E-mail"]

for i in range(6):
    Label(f, text=info[i], width=20).grid(column=0, row=i)
    entry.append(Entry(f, width=20))
    entry[i].grid(column=1, row=i)


Button(f, text="Submit", width=20, command=submit).grid(column=1, row=6)

f.mainloop()
