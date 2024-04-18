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


def total():
    global numbers
    Sum = sum([int(i.get()) for i in numbers])
    Label(f, text=f"Total: {Sum}").pack()


def average():
    global numbers
    Avg = sum([int(i.get()) for i in numbers]) / 5
    Label(f, text=f"Average: {Avg}").pack()


def maxi():
    global numbers
    Max = max([int(i.get()) for i in numbers])
    Label(f, text=f"Maximum: {Max}").pack()


def mini():
    global numbers
    Min = min([int(i.get()) for i in numbers])
    Label(f, text=f"Minimum: {Min}").pack()


numbers = []
for i in range(5):
    numbers.append(Entry(f))
    numbers[i].pack()

Button(f, text="Sum", width=20, command=total).pack()

Button(f, text="Average", width=20, command=average).pack()

Button(f, text="Maximum", width=20, command=maxi).pack()

Button(f, text="Minimum", width=20, command=mini).pack()


f.mainloop()
