import tkinter
win=tkinter.Tk()
win.title("Patient's Past Medical History|Accord Healthcare")
win.geometry('1450x600')

heading=tkinter.Label(win,text="Accord Healthcare",font=("Times New Roman",30))
heading.pack()
heading2=tkinter.Label(win,text="Laboratory Management System",font=("Times New Roman",30))
heading2.pack()
empty=tkinter.Label(win,text="")
empty.place(x=50,y=50)

Medications=tkinter.Label(win,text="Medications Details",font=("Times New Roman",15))
Medications.place(x=50,y=130)
Medications_inp=tkinter.Entry(win,width=90)
Medications_inp.place(x=160,y=160)

Childhood_illness=tkinter.Label(win,text="Childhood Illness?",font=("Times New Roman",15))
Childhood_illness.place(x=50,y=180)
Childhood_illness_inp=tkinter.Entry(win,width=90)
Childhood_illness_inp.place(x=160,y=210)

Allergies=tkinter.Label(win,text="Do you have any allergies?",font=("Times New Roman",15))
Allergies.place(x=50,y=240)
var=tkinter.IntVar()
var1=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var,value=1).place(x=210,y=270)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var1,value=1).place(x=270,y=270)

Allergies_yes=tkinter.Label(win,text="If yes, Allergies Having",font=("Times New Roman",15))
Allergies_yes.place(x=50,y=300)
Allergies_yes_inp=tkinter.Entry(win,width=90)
Allergies_yes_inp.place(x=160,y=330)

Sugeries=tkinter.Label(win,text="Did you undergo any surgery?",font=("Times New Roman",15))
Sugeries.place(x=50,y=360)
var3=tkinter.IntVar()
var4=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var3,value=1).place(x=210,y=390)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var4,value=1).place(x=270,y=390)

Surgeries_yes=tkinter.Label(win,text="If Yes, Sugeries undergone",font=("Times New Roman",15))
Surgeries_yes.place(x=50,y=420)
Surgeries_yes_inp=tkinter.Entry(win,width=90)
Surgeries_yes_inp.place(x=160,y=450)


Hep=tkinter.Label(win,text="Hepatitis B:",font=("Times New Roman",15))
Hep.place(x=790,y=140)
var5=tkinter.IntVar()
var6=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var5,value=1).place(x=990,y=150)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var6,value=1).place(x=1090,y=150)

Influenza=tkinter.Label(win,text="Influenza:",font=("Times New Roman",15))
Influenza.place(x=790,y=200)
var7=tkinter.IntVar()
var8=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var7,value=1).place(x=990,y=210)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var8,value=1).place(x=1090,y=210)

Rubella=tkinter.Label(win,text="Rubella:",font=("Times New Roman",15))
Rubella.place(x=790,y=260)
var9=tkinter.IntVar()
var10=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var9,value=1).place(x=990,y=270)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var10,value=1).place(x=1090,y=270)

RotaVirus=tkinter.Label(win,text="RotaVirus:",font=("Times New Roman",15))
RotaVirus.place(x=790,y=320)
var11=tkinter.IntVar()
var12=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var11,value=1).place(x=990,y=340)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var12,value=1).place(x=1090,y=340)



Immunizations=tkinter.Label(win,text="Other Immunizations Taken:",font=("Times New Roman",15))
Immunizations.place(x=790,y=380)
Immunizations_inp=tkinter.Entry(win,width=100)
Immunizations_inp.place(x=790,y=410)

Diabetes=tkinter.Label(win,text="Are you suffering from diabetes?",font=("Times New Roman",15))
Diabetes.place(x=790,y=440)
var13=tkinter.IntVar()
var14=tkinter.IntVar()
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var13,value=1).place(x=990,y=480)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var14,value=1).place(x=1090,y=480)

bt=tkinter.Button(win,text="Submit",font=("Times New Roman",12))
bt.place(x=700,y=520)

win.mainloop()
