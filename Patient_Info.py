import tkinter
win=tkinter.Tk()
win.title("Patient's Past Medical History|Accord Healthcare")
win.geometry('600x500')

heading=tkinter.Label(win,text="Accord Healthcare",font=("Times New Roman",30))
heading.pack()
heading2=tkinter.Label(win,text="Laboratory Management System",font=("Times New Roman",20))
heading2.pack()

empty=tkinter.Label(win,text="")
empty.pack()
"""
Current_health=tkinter.Label(win,text="What are your current goals for your health?",font=("Times New Roman",15))
Current_health.place(x=50,y=130)
Current_health_inp=tkinter.Entry(win,width=70)
Current_health_inp.place(x=160,y=130)
"""
Medications=tkinter.Label(win,text="Ongoing Medications",font=("Times New Roman",12))
Medications.place(x=50,y=160)
Medications_inp=tkinter.Entry(win,width=60)
Medications_inp.place(x=160,y=190)

Childhood_illness=tkinter.Label(win,text="Childhood Illnesses",font=("Times New Roman",12))
Childhood_illness.place(x=50,y=220)
Childhood_illness_inp=tkinter.Entry(win,width=60)
Childhood_illness_inp.place(x=160,y=250)

Allergies=tkinter.Label(win,text="Allergies",font=("Times New Roman",12))
Allergies.place(x=50,y=280)
var1=tkinter.IntVar()
var2=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",12),padx=5,variable=var1,value=1).place(x=210,y=310)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",12),padx=5,variable=var2,value=1).place(x=270,y=310)

Allergies_yes=tkinter.Label(win,text="If yes, Allergies Having",font=("Times New Roman",15))
Allergies_yes.place(x=50,y=330)
Allergies_yes_inp=tkinter.Entry(win,width=180)
Allergies_yes_inp.place(x=160,y=360)

Sugeries=tkinter.Label(win,text="Have you undergone any surgery",font=("Times New Roman",12))
Sugeries.place(x=50,y=400)
var3=tkinter.IntVar()
var4=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var3,value=1).place(x=300,y=410)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var4,value=1).place(x=350,y=410)

Surgeries_yes=tkinter.Label(win,text="If Yes, Sugeries undergone",font=("Times New Roman",12))
Surgeries_yes.place(x=50,y=450)
Surgeries_yes_inp=tkinter.Entry(win,width=60)
Surgeries_yes_inp.place(x=160,y=490)

Immunizations=tkinter.Label(win,text="Immunizations",font=("Times New Roman",12))
Immunizations.place(x=50,y=520)
Immunizations_inp=tkinter.Entry(win,width=90)
Immunizations_inp.place(x=160,y=550)

Diabetes=tkinter.Label(win,text="Are you suffering from diabetes?",font=("Times New Roman",15))
Diabetes.place(x=50,y=570)
var2=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var2,value=1).place(x=520,y=580)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var2,value=1).place(x=580,y=580)
