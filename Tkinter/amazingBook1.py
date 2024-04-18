import tkinter
from tkinter import ttk

f = tkinter.Tk()
f.title("Test")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 30)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)


def show():
    ttk.Label(f, text=f"{btn.get()}...! It is amazing book").pack()


ttk.Label(f, text="Book name").pack()
btn = ttk.Entry(f, width=20)
btn.insert(0, "book")
btn.pack()

ttk.Button(f, text="Click me", command=show).pack()

f.mainloop()
