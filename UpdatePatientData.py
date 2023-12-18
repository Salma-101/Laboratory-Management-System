import tkinter
win=tkinter.Tk()
win.title("Update Patient Data|Accord Healthcare")
win.geometry('600x500')

heading=tkinter.Label(win,text="Accord Healthcare",font=("Times New Roman",30))
heading.pack()
heading2=tkinter.Label(win,text="Laboratory Management System",font=("Times New Roman",30))
heading2.pack()

empty = tkinter.Label(win,text=" ")
empty.pack()

name =tkinter.Label(win, text="Name:",font=("Times New Roman",14))
name.pack()
name_inp = tkinter.Entry(win, width=40)
name_inp.pack()

Height=tkinter.Label(win,text="Height:",font=("Times New Roman",15))
Height.pack()
Height_inp=tkinter.Entry(win,width=40)
Height_inp.pack()

Weight=tkinter.Label(win,text="Weight:",font=("Times New Roman",15))
Weight.pack()
Weight_inp=tkinter.Entry(win,width=40)
Weight_inp.pack()

Lab_test_conducted=tkinter.Label(win,text="Lab Test Conducted:",font=("Times New Roman",15))
Lab_test_conducted.pack()
Lab_test_conducted_inp=tkinter.Entry(win,width=40)
Lab_test_conducted_inp.pack()

Test_result=tkinter.Label(win,text="Test Result:",font=("Times New Roman",15))
Test_result.pack()
Test_result_inp=tkinter.Entry(win,width=40)
Test_result_inp.pack()

Normal_range=tkinter.Label(win,text="Normal Range:",font=("Times New Roman",15))
Normal_range.pack()
Normal_range_inp=tkinter.Entry(win,width=40)
Normal_range_inp.pack()

Unit=tkinter.Label(win,text="Unit:",font=("Times New Roman",15))
Unit.pack()
unit_np=tkinter.Entry(win,width=40)
unit_np.pack()

empty = tkinter.Label(win,text=" ")
empty.pack()

def UpdateData():
    Label("Data Added").pack()
    entered_data = {"Name":name_inp.get(),"Height":Height_inp.get(),"Weight":Weight_inp.get(),"Lab Test Conducted":Lab_test_conducted_inp.get(),"Test Result":Test_result_inp.get(),"Normal Range":Normal_range_inp.get(),"Unit":unit_np.get()}
    fields = ["Name","Height","Weight","Lab Test Conducted","Test Result","Normal Range","Unit"]
    with open("UpdateData.csv",'w') as csvfile4:
        csvwriter = csv.DictWriter(csvfile4,fieldnames = fields)
        csvwriter.writerow(entered_data)
bt=tkinter.Button(win,text="Submit",font=("Times New Roman",12))
bt.pack()
