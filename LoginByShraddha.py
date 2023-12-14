import tkinter as tk
from tkinter import messagebox
def validate_login():
    
    username = username_entry.get()
    password = password_entry.get()

    
    if username=="admin" and password=="admin":
                messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
      
    else:
        
        messagebox.showerror("Login Failed", "Invalid username or password")

win = tk.Tk()
win.title("Patient Login | Accord Healthcare")
win.geometry('400x300')

username_label = tk.Label(win, text="Username:", font=('Times New Roman',30))
username_label.grid(row=0, column=0, padx=40, pady=20)

username_entry = tk.Entry(win)
username_entry.grid(row=0, column=1, padx=40, pady=20)

password_label = tk.Label(win, text="Password:", font=('Times New Roman',30))
password_label.grid(row=1, column=0, padx=40, pady=20)

password_entry = tk.Entry(win, show="*")
password_entry.grid(row=1, column=1, padx=40, pady=20)


login_button = tk.Button(win, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=20)

win.mainloop()
