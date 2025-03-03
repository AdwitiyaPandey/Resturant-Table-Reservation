from tkinter import *
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

"""
Author: Tsewang Bista
Created on: 2025-02-25
Description: Restaurant Table Booking System using Tkinter and MySQL.
"""

# Database Connection Function
def db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='restaurant_booking',
            user='root',  # Update this if using another user
            password=''   # Set your MySQL password
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None

# Function to Submit Data
def submit_data():
    name = e1.get()
    contact = e2.get()
    location = e3.get()
    date = e4.get()  # Ensure this is in 'YYYY-MM-DD' format for MySQL
    guests = e6.get()
    time_selected = time_dropdown.get()

    try:
        connection = db_connection()
        if connection is None:
            print("Error: Unable to connect to database.")
            return
        
        cursor = connection.cursor()
        sql_insert_query = """INSERT INTO bookings (name, contact, location, date, guests, time1)
                              VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql_insert_query, (name, contact, location, date, guests, time_selected))
        connection.commit()
        messagebox.showinfo("Success", "Reservation Successful!")
        cursor.close()
    except Error as e:
        messagebox.showerror("Error", f"Failed to insert record: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()

# Tkinter GUI Setup
root = Tk()
root.title("Restaurant Table Booking System")
root.iconbitmap("table.ico")
root.geometry("600x400")
root.resizable(0, 0)

# Load Image Background
image_path = r"/Users/tsewangbista/Desktop/backend/F511855D-6DBD-4004-A4C4-CBABF487CFA2.jpeg"
image = Image.open(image_path)
image = image.resize((283, 600))
bg_image = ImageTk.PhotoImage(image)

bg_label = Label(root, image=bg_image)
bg_label.pack(side="left", fill="y")
root.config(bg="Dark cyan")

# Time Dropdown
choices = ['12:00 PM', '12:30 PM', '1:00 PM', '1:30 PM', '2:00 PM', '2:30 PM', '3:00 PM', '3:30 PM', '4:00 PM', 
           '4:30 PM', '5:00 PM', '5:30 PM', '6:00 PM', '6:30 PM', '7:00 PM', '7:30 PM', '8:00 PM', '8:30 PM', 
           '9:00 PM', '9:30 PM', '10:00 PM', '10:30 PM', '11:00 PM', '11:30 PM']
time_dropdown = ttk.Combobox(root, values=choices)
time_dropdown.place(x=420, y=210)

# Labels & Entry Fields
Label(root, text="Dine Reserve", font="Lobster 15 bold", bg="Dark cyan").pack()
Label(text="Name", font="Garamond 10 bold", bg="Dark cyan").place(x=288, y=50)
Label(text="Contact", font="Garamond 10 bold", bg="Dark cyan").place(x=288, y=90)
Label(text="Location, Restaurant", font="Garamond 10 bold", bg="Dark cyan").place(x=288, y=130)
Label(text="Date (YYYY-MM-DD)", font="Garamond 10 bold", bg="Dark cyan").place(x=288, y=170)
Label(text="Time", font="Garamond 10 bold", bg="Dark cyan").place(x=288, y=210)
Label(text="Guests", font="Garamond 10 bold", bg="Dark cyan").place(x=288, y=250)

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

# Submit Button
submit_button = Button(root, text="DINE-IN", command=submit_data, bg="Gray")
submit_button.place(x=400, y=350)

# Main Loop
root.mainloop()
