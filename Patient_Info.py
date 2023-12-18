import tkinter
import csv
win=tkinter.Tk()
win.title("Patient's Past Medical History|Accord Healthcare")
win.geometry('1450x600')

heading=tkinter.Label(win,text="Accord Healthcare",font=("Times New Roman",30))
heading.pack()
heading2=tkinter.Label(win,text="Laboratory Management System",font=("Times New Roman",27))
heading2.pack()

name=tkinter.Label(win,text="Name:",font=("Times New Roman",13))
name.place(x=50,y=95)
name_inp = tkinter.Entry(win,width=40)
name_inp.place(x=120,y=98)

Medications=tkinter.Label(win,text="Medications Details",font=("Times New Roman",15))
Medications.place(x=50,y=130)
Medications_inp=tkinter.Entry(win,width=90)
Medications_inp.place(x=160,y=160)

Childhood_illness=tkinter.Label(win,text="Childhood Illnesses",font=("Times New Roman",15))
Childhood_illness.place(x=50,y=180)
Childhood_illness_inp=tkinter.Entry(win,width=90)
Childhood_illness_inp.place(x=160,y=210)

Allergies_yes=tkinter.Label(win,text="If yes, Allergies Having",font=("Times New Roman",15))
Allergies_yes.place(x=50,y=300)
Allergies_yes_inp=tkinter.Entry(win,width=90)
Allergies_yes_inp.place(x=160,y=330)

Allergies=tkinter.Label(win,text="Do you have any allergies?",font=("Times New Roman",15))
Allergies.place(x=50,y=240)
var0=tkinter.StringVar()
var0.set(None)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var0,value="No").place(x=270,y=270)
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var0,value="Yes").place(x=210,y=270)

Surgeries_yes=tkinter.Label(win,text="If Yes, Sugeries undergone",font=("Times New Roman",15))
Surgeries_yes.place(x=50,y=420)
Surgeries_yes_inp=tkinter.Entry(win,width=90)
Surgeries_yes_inp.place(x=160,y=450)

Sugeries=tkinter.Label(win,text="Did you undergo any surgery?",font=("Times New Roman",15))
Sugeries.place(x=50,y=360)
var1=tkinter.StringVar()
var1.set(None)
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var1,value="Yes").place(x=210,y=390)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var1,value="No").place(x=270,y=390)

Hep=tkinter.Label(win,text="Hepatitis B:",font=("Times New Roman",15))
Hep.place(x=790,y=140)
var2=tkinter.StringVar()
var2.set(None)
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var2,value="Yes").place(x=990,y=150)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var2,value="No").place(x=1090,y=150)

Influenza=tkinter.Label(win,text="Influenza:",font=("Times New Roman",15))
Influenza.place(x=790,y=200)
var3=tkinter.StringVar()
var3.set(None)
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var3,value="Yes").place(x=990,y=210)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var3,value="No").place(x=1090,y=210)

Rubella=tkinter.Label(win,text="Rubella:",font=("Times New Roman",15))
Rubella.place(x=790,y=260)
var4=tkinter.StringVar()
var4.set(None)
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var4,value="Yes").place(x=990,y=270)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var4,value="No").place(x=1090,y=270)

RotaVirus=tkinter.Label(win,text="RotaVirus:",font=("Times New Roman",15))
RotaVirus.place(x=790,y=320)
var5=tkinter.StringVar()
var5.set(None)
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var5,value="Yes").place(x=990,y=340)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var5,value="No").place(x=1090,y=340)

Immunizations=tkinter.Label(win,text="Other Immunizations Taken:",font=("Times New Roman",15))
Immunizations.place(x=790,y=380)
Immunizations_inp=tkinter.Entry(win,width=100)
Immunizations_inp.place(x=790,y=410)

Diabetes=tkinter.Label(win,text="Diabetic?",font=("Times New Roman",15))
Diabetes.place(x=790,y=440)
var6=tkinter.StringVar()
var6.set(None)
tkinter.Radiobutton(win,text="Yes",font=("Times New Roman",11),padx=5,variable=var6,value="Yes").place(x=990,y=480)
tkinter.Radiobutton(win,text="No",font=("Times New Roman",11),padx=5,variable=var6,value="No").place(x=1090,y=480)

def PatientInfo():
    tkinter.Label(win, text="Patient Info Generated").place(x=615,y=560)
    if var6.get()==None: var6.get()=="No"
    else: var6.get()=="Yes"
    fields = ["Name","Medication Details","Childhood Illnesses","Allergies","Surgeries","Hepatitis B","Influenza","Rubella","RotaVirus","Other Immunisations Taken","Diabetic"]
    entered_data = {"Name":name_inp.get(),"Medication Details":Medications_inp.get(),"Childhood Illnesses":Childhood_illness_inp.get(),"Allergies":var0.get(),"Allergies":Allergies_yes_inp.get(),"Surgeries":var1,"Surgeries":Surgeries_yes_inp.get(),"Hepatitis B":var2.get(),"Influenza":var3.get(),"Rubella":var4.get(),"RotaVirus":var5.get(),"Other Immunisations Taken":Immunizations_inp.get(),"Diabetic":var6.get()}
    with open("Patient-Infos.csv",'a') as csvfile2:
        csvwriter = csv.DictWriter(csvfile2,fieldnames=fields)
        csvwriter.writerow(entered_data)

bt=tkinter.Button(win,text="Submit",font=("Times New Roman",12), command=PatientInfo)
bt.place(x=650,y=520)

win.mainloop()
