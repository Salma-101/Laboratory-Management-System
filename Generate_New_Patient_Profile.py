
# GENERATE NEW PATIENT PROFILE

from tkinter import *
import csv

win = Tk()
win.title("Generate New Patient Profile | Accord Healthcare")
win.geometry('700x700')

heading = Label(win, text="Accord Healthcare", font=("Times New Roman",30))
heading.pack()

heading2 = Label(win, text="Laboratory Management System", font=("Times New Roman",20))
heading2.pack()

empty = Label(win, text="")
empty.pack()
"""
P_ID = Label(win, text="Patient ID")
P_ID.pack()
P_ID_num = Label(win, text="110265")
P_ID_num.pack()
"""
P_Name = Label(win, text="Patient Name", font=("Times New Roman",12))
P_Name.place(x=5,y=130)
P_Name_inp = Entry(win, width=20)
P_Name_inp.place(x=160,y=130)

P_DOB = Label(win, text="Date Of Birth", font=("Times New Roman",12))
P_DOB.place(x=5,y=160)
P_DOB_inp = Entry(win, width=20)
P_DOB_inp.place(x=160,y=160)

P_Email = Label(win, text="Email ID", font=("Times New Roman",12))
P_Email.place(x=5, y=190)
P_Email_inp = Entry(win)
P_Email_inp.place(x=160,y=190)

P_Num = Label(win, text="Mobile Number", font=("Times New Roman",12))
P_Num.place(x=5,y=220)
P_Num_inp = Entry(win)
P_Num_inp.place(x=160,y=220)

Gender = Label(win, text="Gender", font=("Times New Roman",12))
Gender.place(x=5,y=250)
var=StringVar()
var.set(None)
rm = Radiobutton(win, text="Male", variable=var,value="Male")
rm.place(x=148,y=250)
rf = Radiobutton(win, text="Female", variable=var,value="Female")
rf.place(x=210,y=250)

P_Address = Label(win, text="Address", font=("Times New Roman",12))
P_Address.place(x=5,y=280)
P_Address_inp = Entry(width=60)
P_Address_inp.place(x=160,y=280)

P_City = Label(win, text="City", font=("Times New Roman",12))
P_City.place(x=5,y=310)
P_City_inp = Entry(win)
P_City_inp.place(x=160,y=310)

List_of_states = ["","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
cv = StringVar()
drplist = OptionMenu(win, cv, *List_of_states)
drplist.config()
cv.set("")
P_State = Label(win, text="State", font=("Times New Roman",12))
P_State.place(x=5,y=340)
drplist.place(x=154,y=335)

def Generate_Profile():
    Label(win, text="Profile Generated").place(x=180,y=420)
    if var.get()=="1": var.get()== "Male"
    else: var.get()== "Female"
    entered_data = {"Patient Name":P_Name_inp.get(),"Date of Birth":P_DOB_inp.get(),"Email ID":P_Email_inp.get(),"Mobile Number":P_Num_inp.get(),"Gender":var.get(),"Address":P_Address_inp.get(),"City":P_City_inp.get(),"State":cv.get()}
    fields = ["Patient Name","Date of Birth","Email ID","Mobile Number","Gender","Address","City","State"]

    with open("Patient_Details.csv",'a') as csvfile1:
        csvwriter = csv.DictWriter(csvfile1,fieldnames = fields)
        csvwriter.writerow(entered_data)
        
bt = Button(win, text="Generate Profile", font=("Times New Roman",12), command=Generate_Profile)
bt.place(x=180,y=380)

win.mainloop()
