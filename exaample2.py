from tkinter import *

# Function to display "Login Successful" with the entered name
def login_successful():
    entered_name = e1.get()  # Get the text from the entry field
    if entered_name:  # Check if a name is entered
        success_message = f"Login Successful, {entered_name}!"
    else:
        success_message = "Login Successful, Guest!"
    
    label_success = Label(root, text=success_message, fg="green")
    label_success.place(x=30, y=200)

root = Tk()
root.geometry("300x300")  # Set the window size

# Name label and entry field
name = Label(root, text="Name")
name.place(x=30, y=50)
e1 = Entry(root)
e1.place(x=100, y=50)

# Login button with callback
Button(root, text="Log in", width=20, command=login_successful).place(x=30, y=170)

root.mainloop()
