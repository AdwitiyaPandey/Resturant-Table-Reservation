from tkinter import *
from tkinter import messagebox


def new_window():
    new_window = Toplevel()
    new_window.geometry("200x200")
    new_window.title("New Window")
    Label(new_window, text="This is a new window").pack()

    new_window()



def checkPass():
    if(e1.get()=='user' and e2.get()=='1234'):
        new_window()
    else:
        messagebox.showerror("Login",'Incorrect Password')

root = Tk()
root.geometry("300x300")
name = Label(root, text = "Name")
name.pack()
e1 = Entry(root)
e1.pack()
password = Label(root, text = "Password")
password.pack()
e2 = Entry(root)
e2.pack()
w = Button(root, text="Log in", width=20, command=checkPass).pack()

root.mainloop()