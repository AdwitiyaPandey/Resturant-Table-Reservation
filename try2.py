from tkinter import *
def login_successful():
    entered_name = e1.get()
    selected_role = role_var.get() 
    if entered_name:  
        success_message = f"Login Successful, {entered_name}!"
        
        
    
    label_success = Label(root, text="Login Successful", fg="green")
    label_success.place(x=30, y=230)
    label_success.config(text=f"Login Successful, {entered_name} ({selected_role})", fg="green")

root = Tk()

root.geometry("300x300")  

name = Label(root, text="Name")
name.place(x=30, y=50)
e1 = Entry(root)
e1.place(x=100, y=50)
role_var = StringVar(value="User")
Label(root, text="Select Role:").place(x=30, y=100)
Radiobutton(root, text="Male", variable=role_var, value="Male").place(x=30, y=130)
Radiobutton(root, text="Female", variable=role_var, value="User").place(x=30, y=160)
Radiobutton(root, text="Others", variable=role_var, value="Other").place(x=30, y=190)


Button(root, text="Log in", width=20, command=login_successful).place(x=30, y=250)
mainloop()