# * for everything
from tkinter import *

# importing messagebox
from tkinter import messagebox

# main Window
age_app = Tk() #could be root / age_app

# Change app Title
age_app.title("Joe Cal Age")

# Set Dimensions of the window
age_app.geometry("400x200")

# Write age label and design it
the_label = Label(age_app, text="Write Your Age: ", height=2, font=("Arial", 20))
the_label.pack() # To add the label in window

# Age variable
age = StringVar()

# Set defualt value for Age
age.set("")

# Create the input & width for Carachter
age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable=age)
age_input.pack() # To add the input in window

def cal():
    # get age in years
    the_age_value = age.get()

    # get time units
    months = int(the_age_value) * 12
    weeks = months * 4
    days = int(the_age_value) * 365

    line1 = f"Your Age in Months: {months}"
    line2 = f"Your Age in Weeks: {weeks}"
    line3 = f"Your Age in Days: {days}"

    all_lines = [line1, line2, line3]

    # Show Messagebox and adding Lines 
    messagebox.showinfo("Your Age:", "\n".join(all_lines))


# Create the Calculate Button bg for background fg for font ground
btn = Button(age_app, text="Calculate", width= 10, height=2, bg="#e91e63", fg="white", borderwidth=0, command=cal)
btn.pack()

# Running for infinity
age_app.mainloop()

