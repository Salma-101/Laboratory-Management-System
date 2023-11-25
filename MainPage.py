
# MAIN PAGE

from tkinter import *

win = Tk()
win.title("Accord Healthcare | Laboratory Management System")
win.geometry('500x300')

heading = Label(win, text="Accord Healthcare", font=("Times New Roman",35))
heading.pack()

empty = Label(win, text="")
empty.pack()

b1 = Button(win, text="Generate New Patient Profile", fg="green")
b1.pack()
b2 = Button(win, text="Enter Patient Info", fg="green")
b2.pack()
b3 = Button(win, text="Update Patient Data", fg="green")
b3.pack()
b4 = Button(win, text="Patient Test Results", fg="green")
b4.pack()
b5 = Button(win, text="Patient Invoice", fg="green")
b5.pack()
