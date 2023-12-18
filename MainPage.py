
# MAIN PAGE

from tkinter import *

win = Tk()
win.title("Accord Healthcare | Laboratory Management System")
win.geometry('700x700')

heading = Label(win, text="Accord Healthcare", font=("Times New Roman",35))
heading.pack()

heading2 = Label(win, text="Laboratory Management System", font=("Times New Roman",26))
heading2.pack()

empty = Label(win, text="")
empty.pack()

def Generate_New_Patient_Profile():
    import Generate_New_Patient_Profile

def Patient_Info():
    import Patient_Info

def UpdateData():
    import UpdatePatientData

def ViewData():
    import TreeViewData

def TestResults():
    __import__('Patient Test Results.py')

def Invoice():
    import InvoiceByDhatri

b1 = Button(win, text="Generate New Patient Profile", fg="green", font=("Times New Roman",13), command = Generate_New_Patient_Profile)
b1.pack()
empty = Label(win, text=" ",font=1)
empty.pack()
b2 = Button(win, text="Enter Patient Info", fg="green", font=("Times New Roman",13), command = Patient_Info)
b2.pack()
empty = Label(win, text="",font=1)
empty.pack()
b3 = Button(win, text="Update Patient Data", fg="green", font=("Times New Roman",13), command=UpdateData)
b3.pack()
empty = Label(win, text="",font=1)
empty.pack()
b4 = Button(win, text="View Patients Data", fg="green", font=("Times New Roman",13),command=ViewData)
b4.pack()
empty = Label(win, text="",font=1)
empty.pack()
b5 = Button(win, text="Patient Test Results", fg="green", font=("Times New Roman",13), command=TestResults)
b5.pack()
empty = Label(win, text="",font=1)
empty.pack()
b6 = Button(win, text="Patient Invoice", fg="green", font=("Times New Roman",13),command=Invoice)
b6.pack()

win.mainloop()
