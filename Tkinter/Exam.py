import tkinter
from tkinter import *
from tkinter import ttk


f = tkinter.Tk()
f.title("Exam")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)

questions = ["How are you?", "How is today?", "How old are you?"]
answers = [["Good", "Fine", "Great"], [
    "Bad", "Nice", "Busy"], ["15", "18", "20"], ]

global n
n = 0


def nextQ():
    global n, buttons
    n += 1
    if len(questions) > n:
        lb.configure(text=questions[n])
        for i in range(1, len(answers[0]) + 1):
            buttons[i-1].configure(text=answers[n][i-1])
    else:
        lb.configure(text="End of Questions")
        for i in range(1, len(answers[0]) + 1):
            buttons[i-1].destroy()

        bt.destroy()


lb = ttk.Label(f, text=questions[0])

lb.pack()

selected = IntVar()

global buttons
buttons = []
for i in range(1, len(answers[0]) + 1):
    buttons.append(ttk.Radiobutton(
        f, text=answers[0][i-1], value=i, variable=selected))
    buttons[i-1].pack()

bt = ttk.Button(f, text="Next", command=nextQ)
bt.pack()

f.mainloop()
