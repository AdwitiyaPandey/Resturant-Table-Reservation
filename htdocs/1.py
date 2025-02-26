from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
"""
Restaurant Table Booking System - GUI
This script creates a Tkinter-based graphical user interface (GUI) for users to book tables at a restaurant.

Features:
- Background image for UI aesthetics
- Labels and input fields for user details (Name, Contact, Location, Date, Time, Guests)
- Dropdown selection for time slots
- Basic UI setup using Tkinter and ttk widgets

Author: [Adwitiya Pandey]
Date: [2025-02-11]
"""


root = Tk()
root.title("Restaurant Table Booking System")
root.iconbitmap("table.ico")
root.geometry("600x400")
root.resizable(0, 0)
image_path = r"C:\Users\HP Victus\OneDrive\Desktop\tikinterpyhton\725c86e86ca1f893f506c1fbe0b37359.jpg"
image = Image.open(image_path)
image = image.resize((283, 600))  
bg_image = ImageTk.PhotoImage(image)

bg_label = Label(root, image=bg_image)
bg_label.pack(side="left", fill="y") 
root.config(bg="Dark cyan")

choices = [  
    "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM", "3:00 PM", 
    "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM", 
    "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM", "9:30 PM", "10:00 PM", 
    "10:30 PM", "11:00 PM", "11:30 PM"
]

time_dropdown = ttk.Combobox(root, values=choices)
time_dropdown.set("Select Time")  # Default placeholder
time_dropdown.place(x=420, y=210)






Label(root, text="Dine Reserve", font="Lobster 15 bold",bg= "Dark cyan").pack()
Label(text="Name", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=50)
Label(text="Contact", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=90)
Label(text="Location, Restaurant", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=130)
Label(text="Date (YYYY-MM-DD)", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=170)
Label(text="Time", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=210)
Label(text="Guests", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=250)

e1 = Entry(root) 
e1.place(x=420, y=50)
e2 = Entry(root)
e2.place(x=420, y=90)
e3 = Entry(root)
e3.place(x=420, y=130)
e4 = Entry(root)
e4.place(x=420, y=170)
e6 = Entry(root)
e6.place(x=420, y=250)

root.mainloop()
