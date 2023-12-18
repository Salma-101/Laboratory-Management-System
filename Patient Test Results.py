import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
from tkcalendar import Calendar

wn = Tk()
wn.title("patient test result Generators")
wn.geometry("750x800")
wn.configure(bg='light grey')

Label(wn, text="PATIENT DETAILS ", font=("calibre", 30, "bold"), bg="light grey", fg="black").place(x=150, y=10)
Label(wn, text="Patient Name", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=80)
patient_name = Entry(wn, font=("calibre", 15))
patient_name.place(x=270, y=80, width=300, height=35)

Label(wn, text="Age", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=140)
age = Entry(wn, font=("calibre", 15))
age.place(x=270, y=140, width=300, height=35)


selected_date = StringVar()

date = Label(wn, textvariable=selected_date, font=("calibre", 15))
date.place(x=270, y=320)

def selectDate():
    root = Tk()
    root.geometry("400x400")

    cal = Calendar(root, selectmode='day', year=2023, month=12, day=18)
    cal.pack(pady=20)

    def grad_date():
        selected_date.set(str(cal.get_date()))
        root.destroy()  # Close the date selection window

    Button(root, text="Get Date", command=grad_date).pack(pady=20)
    root.mainloop()

Label(wn, text="DOB", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=200)
Button(wn, text="Select Date", font=("calibre", 14), command=selectDate).place(x=450, y=200)

Label(wn, text="Phone No", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=260)

phNo = Entry(wn, font=("calibre", 15))
phNo.place(x=270, y=260, width=300, height=35)



Label(wn, text="Patient Image", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=320)

# ==== Browse File
def browseFiles():
    global wn, file_name
    file_name = filedialog.askopenfilename(title="Select your File")
    Label(wn, text=os.path.basename(file_name), font=("calibre", 15)).place(x=270, y=360)

Button(wn, text="Browse Files", font=("calibre", 14), command=browseFiles).place(x=270, y=320)

# ==== Order Details Entry
Label(wn, text="S.no", font=("calibre", 15), bg="light grey", fg="black").place(x=270, y=420)
Label(wn, text="test Type", font=("calibre", 15), bg="light grey", fg="black").place(x=330, y=420)
Label(wn, text="Result", font=("calibre", 15), bg="light grey", fg="black").place(x=450, y=420)
Label(wn, text="Test Details", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=450)

test_sno = Entry(wn, font=("calibre", 15))
test_sno.place(x=270, y=450, width=50, height=35)
test_name = Entry(wn, font=("calibre", 15))
test_name.place(x=330, y=450, width=100, height=35)
test_Result = Entry(wn, font=("calibre", 15))
test_Result.place(x=450, y=450, width=80, height=35)

orders_list = []

def addOrder():
    sno = test_sno.get()
    name = test_name.get()
    result = test_Result.get()

    if sno and name and result:
        orders_list.append((sno, name, result))
        clearOrderFields()
        print("test details added successfully.")
    else:
        print("Please fill in all order details.")

def clearOrderFields():
    test_sno.delete(0, END)
    test_name.delete(0, END)
    test_Result.delete(0, END)

# ==== Order Buttons
Button(wn, text="Add test", font=("calibre", 14), command=addOrder).place(x=650, y=450)

# ... (Existing code for the rest of the GUI)

def generateInvoice():
    global file_name, patient_name, age, date, phNo, auSign

    try:
        inv_canvas = canvas.Canvas("Test_Result.pdf", pagesize=(200, 250), bottomup=0)

        inv_canvas.line(5, 45, 195, 45)
        inv_canvas.line(15, 120, 185, 120)
        inv_canvas.line(35, 108, 35, 220)
        inv_canvas.line(115, 108, 115, 220)
        inv_canvas.line(135, 108, 135, 220)
        inv_canvas.line(160, 108, 160, 220)
        inv_canvas.line(15, 220, 185, 220)

        inv_canvas.translate(10, 40)
        inv_canvas.scale(1, -1)
        inv_canvas.drawImage(file_name, 0, 0, width=50, height=30)
        inv_canvas.scale(1, -1)
        inv_canvas.translate(-10, -40)
        inv_canvas.setFont("Times-Bold", 9)
        inv_canvas.drawCentredString(125, 20,"Patient Name :" + patient_name.get())
        inv_canvas.setFont("Times-Bold", 7)
        inv_canvas.drawCentredString(125, 30,"Age :" + age.get())
        inv_canvas.setFont("Times-Bold", 8)
        inv_canvas.drawCentredString(100, 55, "Results")
        inv_canvas.setFont("Times-Bold", 6)
        inv_canvas.drawRightString(70, 90, "DOB :")
        inv_canvas.drawRightString(100, 90, date.cget("text"))
        inv_canvas.drawRightString(70, 100, "Phone No. :")
        inv_canvas.drawRightString(100, 100, phNo.get())

        inv_canvas.roundRect(15, 108, 170, 130, 10, fill=0)

        inv_canvas.setFont("Times-Bold", 6)
        inv_canvas.drawCentredString(25, 118, "S.No.")
        inv_canvas.drawCentredString(75, 118, "tests")
        inv_canvas.drawCentredString(173, 118, "Result")

        for idx, order in enumerate(orders_list):
            sno, name, result = order  # Unpack three elements instead of five
            inv_canvas.drawCentredString(25, 128 + idx * 10, sno)
            inv_canvas.drawCentredString(75, 128 + idx * 10, name)
            inv_canvas.drawCentredString(173, 128 + idx * 10, result)  # Use 'result' instead of 'total'


        inv_canvas.showPage()
        inv_canvas.save()

        print("Invoice generated successfully.")
    except Exception as e:
        print(f"Error generating invoice: {e}")
# ====submit details
Button(wn, text="Submit Details", font=("calibre", 14), cursor="hand2", command=generateInvoice).place(x=50, y=550, width=180, height=40)        
wn.mainloop()
