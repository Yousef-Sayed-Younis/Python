import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

f = tkinter.Tk()
f.title("Your Hobby")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 30)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def test():
    let = 'fsrwbv'
    if ent.get()[0].lower() in let:
        showinfo("Hobby", f"Your  Hobby is {ent.get()}")
    else:
        showinfo("Hobby", "It is a New Hobby")


ttk.Label(f, text="Enter Your Hobby").pack()

ent = ttk.Entry(f, width=20)
ent.insert(0, "Hobby")
ent.pack()

Button(f, text="Click", command=test).pack()

f.mainloop()
