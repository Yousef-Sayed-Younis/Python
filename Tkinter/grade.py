import tkinter
from tkinter import *
from tkinter import ttk

f = tkinter.Tk()
f.title("Show Grade")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def show():
    ttk.Label(f, text=f"Your Grade is {clicked.get()}").pack()


ttk.Label(f, text="Choose Your Grade").pack()

grades = ["Excellent", "Very Good", "Good", "Pass", "Fail"]

clicked = StringVar()
clicked.set("Good")

lbx = OptionMenu(f, clicked, *grades).pack()

Button(f, text="Show Grade", command=show).pack()

f.mainloop()
