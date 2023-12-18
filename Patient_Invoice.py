import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
from tkcalendar import Calendar

wn = Tk()
wn.title("Python Invoice Generators")
wn.geometry("750x800")
wn.configure(bg='light grey')

Label(wn, text="Enter patient details ", font=("calibre", 30, "bold"), bg="light grey", fg="black").place(x=100, y=10)
Label(wn, text="Patient Name", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=80)

patient_name = Entry(wn, font=("calibre", 15))
patient_name.place(x=270, y=80, width=300, height=35)
Label(wn, text="Address", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=140)

address = Entry(wn, font=("calibre", 15))
address.place(x=270, y=140, width=300, height=35)
Label(wn, text="City", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=200)

city = Entry(wn, font=("calibre", 15))
city.place(x=270, y=200, width=300, height=35)
Label(wn, text="Patient ID", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=260)

patient_id = Entry(wn, font=("calibre", 15))
patient_id.place(x=270, y=260, width=300, height=35)

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

Label(wn, text="Date", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=320)
Button(wn, text="Select Date", font=("calibre", 14), command=selectDate).place(x=450, y=320)

Label(wn, text="Phone No", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=380)

phNo = Entry(wn, font=("calibre", 15))
phNo.place(x=270, y=380, width=300, height=35)
Label(wn, text="Guardian Name", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=440)

guardian_name = Entry(wn, font=("calibre", 15))
guardian_name.place(x=300, y=440, width=300, height=35)
Label(wn, text="Authorized Signatory", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=500)

auSign = Entry(wn, font=("calibre", 15))
auSign.place(x=270, y=500, width=300, height=35)
Label(wn, text="Patient Image", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=560)

# ==== Browse File
def browseFiles():
    global wn, file_name
    file_name = filedialog.askopenfilename(title="Select your File")
    Label(wn, text=os.path.basename(file_name), font=("calibre", 15)).place(x=270, y=600)

Button(wn, text="Browse Files", font=("calibre", 14), command=browseFiles).place(x=270, y=560)

# ==== test Details Entry
Label(wn, text="S.no", font=("calibre", 15), bg="light grey", fg="black").place(x=270, y=630)
Label(wn, text="test", font=("calibre", 15), bg="light grey", fg="black").place(x=330, y=630)
Label(wn, text="Price", font=("calibre", 15), bg="light grey", fg="black").place(x=440, y=630)
Label(wn, text="Qty", font=("calibre", 15), bg="light grey", fg="black").place(x=500, y=630)
Label(wn, text="Total", font=("calibre", 15), bg="light grey", fg="black").place(x=560, y=630)
Label(wn, text="Payment Details", font=("calibre", 15), bg="light grey", fg="black").place(x=50, y=660)

test_sno = Entry(wn, font=("calibre", 15))
test_sno.place(x=270, y=660, width=50, height=35)
test_name = Entry(wn, font=("calibre", 15))
test_name.place(x=330, y=660, width=100, height=35)
test_price = Entry(wn, font=("calibre", 15))
test_price.place(x=440,y=660, width=50, height=35)
test_qty = Entry(wn, font=("calibre", 15))
test_qty.place(x=500, y=660, width=50, height=35)
test_total = Entry(wn, font=("calibre", 15))
test_total.place(x=560, y=660, width=80, height=35)

tests_list = []

def addtest():
    sno = test_sno.get()
    name = test_name.get()
    price = test_price.get()
    qty = test_qty.get()
    total = test_total.get()

    if sno and name and price and qty and total:
        tests_list.append((sno, name, price, qty, total))
        cleartestFields()
        print("test added successfully.")
    else:
        print("Please fill in all test details.")

def cleartestFields():
    test_sno.delete(0, END)
    test_name.delete(0, END)
    test_price.delete(0, END)
    test_qty.delete(0, END)
    test_total.delete(0, END)

# ==== test Buttons
Button(wn, text="Add test", font=("calibre", 14), command=addtest).place(x=650, y=660)
Button(wn, text="Clear tests", font=("calibre", 14), command=cleartestFields).place(x=650, y=7000)

# ... (Existing code for the rest of the GUI)

def generateInvoice():
    global file_name, patient_name, address, city, patient_id, date, guardian_name, phNo, auSign

    try:
        inv_canvas = canvas.Canvas("patient_Invoice.pdf", pagesize=(200, 250), bottomup=0)

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
        inv_canvas.setFont("Times-Bold", 10)
        inv_canvas.drawCentredString(125, 20, "Patient name :" + patient_name.get())
        inv_canvas.setFont("Times-Bold", 5)
        inv_canvas.drawCentredString(125, 30,"address :" + address.get())
        inv_canvas.drawCentredString(125, 35, city.get() + ", India")
        inv_canvas.setFont("Times-Bold", 6)
        inv_canvas.drawCentredString(125, 42, "Patient Id:" + patient_id.get())
        inv_canvas.drawRightString(70, 80, "Guardian Name :")
        inv_canvas.drawRightString(100, 80, guardian_name.get())
        inv_canvas.drawRightString(70, 90, "Date :")
        inv_canvas.drawRightString(100, 90, date.cget("text"))
        inv_canvas.drawRightString(70, 100, "Phone No. :")
        inv_canvas.drawRightString(100, 100, phNo.get())

        inv_canvas.roundRect(15, 108, 170, 130, 10, fill=0)

        inv_canvas.setFont("Times-Bold", 8)
        inv_canvas.drawCentredString(25, 118, "S.No.")
        inv_canvas.drawCentredString(75, 118, "tests")
        inv_canvas.drawCentredString(125, 118, "Price")
        inv_canvas.drawCentredString(148, 118, "Qty.")
        inv_canvas.drawCentredString(173, 118, "Total")

        for idx, test in enumerate(tests_list):
            sno, name, price, qty, total = test
            inv_canvas.drawCentredString(25, 128 + idx * 10, sno)
            inv_canvas.drawCentredString(75, 128 + idx * 10, name)
            inv_canvas.drawCentredString(125, 128 + idx * 10, price)
            inv_canvas.drawCentredString(148, 128 + idx * 10, qty)
            inv_canvas.drawCentredString(173, 128 + idx * 10, total)

        inv_canvas.drawRightString(180, 228, auSign.get())
        inv_canvas.drawRightString(180, 235, "Signature")
        inv_canvas.showPage()
        inv_canvas.save()

        print("Invoice generated successfully.")
    except Exception as e:
        print(f"Error generating invoice: {e}")
# ====submit details
Button(wn, text="Submit Details", font=("calibre", 14), cursor="hand2", command=generateInvoice).place(x=50, y=700, width=180, height=40)        
wn.mainloop()
