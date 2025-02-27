import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Admin Login")
root.geometry("300x150")
tk.Label(root, text="Username:").pack(pady=(10, 0))
username_entry = tk.Entry(root, width=30)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=(5, 0))
password_entry = tk.Entry(root, width=30, show="*")  
password_entry.pack()


def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "1234":  
        messagebox.showinfo("Login Success", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

login_button = tk.Button(root, text="Log-in", command=login)
login_button.pack(pady=10)

root.mainloop()



