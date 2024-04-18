import random
import tkinter
from tkinter import ttk

f = tkinter.Tk()
f.title("Test")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def rand():
    ttk.Label(
        f, text=f"{random.randint(int(btns[0].get()), int(btns[1].get()))}")


btns = []
for i in range(1, 3):
    ttk.Label(f, text=f"Number{i}").grid(column=0, row=i)
    btn = ttk.Entry(f, width=20)
    btns.append(btn)
    btn.insert(0, f"n{i}")
    btn.grid(column=1, row=i)

ttk.Button(f, text="Generate Random Number",
           command=rand).grid(column=1, row=3)

f.mainloop()
