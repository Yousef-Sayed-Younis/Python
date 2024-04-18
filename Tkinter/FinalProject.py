import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

f = tkinter.Tk()
f.title("Exam")
f.geometry('600x400')
f.config(background="pink")

fnt = ('Times New Roman', 20)
ttk.Style().configure(style='TLabel', font=fnt,
                            background='lightblue', foreground='green')

ttk.Style().configure(style="TEntry", width=4, font=fnt)

answers = []


def clear_frame():
    for w in f.winfo_children():
        w.destroy()


def q1():
    clear_frame()
    Label(f, text="What is the capital of Egypt?").pack()
    global cb
    cb = ttk.Combobox(
        f, values=("Alex", "Cairo", "Damietta"), state="readonly")
    cb.current(0)
    cb.pack()
    Button(f, text="Next", width=20, command=q2).pack()


def q2():
    answers.append(cb.get())
    clear_frame()
    Label(f, text="What is the color of Sky?").pack()
    global lbx
    lbx = Listbox(f)
    ans = ["Red", "Blue", "Yellow", "Green"]
    for i in range(len(ans)):
        lbx.insert(i, ans[i])
    lbx.pack()
    Button(f, text="Next", width=20, command=q3).pack()


def q3():
    answers.append(lbx.get(ACTIVE))
    clear_frame()
    Label(f, text="Where is Makka?").pack()

    global selected
    selected = StringVar()
    selected.set("Egypt")

    ans = ["Egypt", "KSA", "America", "Paris"]

    for i in range(len(ans)):
        Radiobutton(
            f, text=ans[i], value=ans[i], width=20, variable=selected).pack()

    Button(f, text="Next", width=20, command=finish).pack()


def finish():
    answers.append(selected.get())
    clear_frame()
    Label(f, text="With Best Wishes", width=20).pack()
    can = Canvas(f, width=200, height=200)
    can.pack()

    img = PhotoImage(file="flower.png")
    can.create_image(0, 0, image=img, anchor=NW)

    real = ["Cairo", "Blue", "KSA"]
    counter = 0
    for i in range(len(answers)):
        if answers[i] == real[i]:
            counter += 1

    messagebox.showinfo(
        "Result", f"Your Grade is: {(counter / len(answers)) * 100:.2f}%.")


def submit():
    data = [i.get() for i in entries]
    if sel.get() == 0:
        clear_frame()
        Label(f, text="You Must Agree First!", width=20).pack()
    else:
        q1()


info = ["ID", "Name", "Grade"]
hint = ["1000", "Your Name", "first year"]
entries = []
for i in range(3):
    Label(f, text=info[i], width=25).grid(column=0, row=i)
    entries.append(Entry(f, width=27, foreground="gray"))
    entries[i].insert(0, hint[i])
    entries[i].grid(column=1, row=i)

Label(f, text="Are you agree?", width=25, pady=3).grid(column=0, row=3)
sel = IntVar()
chx = Checkbutton(f, text="I Agree", width=20, variable=sel)
chx.grid(column=1, row=3)
Button(f, text="Submit & Next", width=20, command=submit).grid(column=1, row=5)


f.mainloop()
