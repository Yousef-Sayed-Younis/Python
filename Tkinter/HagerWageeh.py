import tkinter
from tkinter import ttk

f = tkinter.Tk()
f.title("Test")
f.geometry('600x400')


def total():
    print("Total degrees:", sum([int(i.get()) for i in btns]))


btns = []
for i in range(1, 6):
    ttk.Label(f, text=f"degree{i}").pack()
    btn = ttk.Entry(f, width=20)
    btns.append(btn)
    btn.insert(0, f"n{i}")
    btn.pack()

ttk.Button(f, text="Total degrees", command=total).pack()

f.mainloop()
