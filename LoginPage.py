# LOGIN

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Accord Healthcare | Laboratory Management System")
root.geometry('700x700')

heading = Label(root, text="Accord Healthcare", font=("Times New Roman",35))
heading.pack()

heading2 = Label(root, text="Laboratory Management System", font=("Times New Roman",26))
heading2.pack()

empty = Label(root, text="")
empty.pack()

login_head = Label(root, text="Admin Login", font=("Times New Roman",23,"underline"))
login_head.pack()

empty = Label(root, text="")
empty.pack()

username = Label(root, text="Username", font=("Times New Roman",17))
username.pack()
username_inp = Entry(root,width=20)
username_inp.pack()

empty = Label(root, text=" ",font=2)
empty.pack()

pswd = Label(root, text="Password", font=("Times New Roman",17))
pswd.pack(padx=20)
pswd_inp = Entry(root,show="*")
pswd_inp.pack(padx=20)

def Main_Page():
    import MainPage

def validate_login():
    
    username = username_inp.get()
    pswd = pswd_inp.get()
    
    if username=="admin" and pswd=="admin":
            messagebox.showinfo("Login Successful", "Welcome!")
            root.withdraw()
            Main_Page()

    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

empty = Label(root, text=" ",font=2)
empty.pack()

login_button = Button(root, text="Login", font=("Times New Roman",13), command=validate_login)
login_button.pack()
