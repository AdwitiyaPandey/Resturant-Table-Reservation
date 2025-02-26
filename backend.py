from tkinter import *
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox, ttk
from datetime import datetime
"""
Author:Tsewang Bista
Created on: 2025-02-25
Description: Restaurant Table Booking System using Tkinter and MySQL. change in different

"""

def submit_data():
    name = e1.get()
    contact = e2.get()
    location = e3.get()
    date = e4.get()  # Ensure this is in 'YYYY-MM-DD' format for MySQL
    guests = e6.get() #post()
    time_selected = time_dropdown.get()

    try: #learn more about try and except and finally
        connection = mysql.connector.connect(
            host='localhost',
            database='restaurant_booking',
            user='root', #use restaurant username
            password=''  #use sql password 101everest and 102kcf
        )

        if connection.is_connected():
            cursor = connection.cursor() 
            sql_insert_query = """ INSERT INTO bookings (name, contact, location, date, guests, time1)
                                   VALUES (%s, %s, %s, %s, %s, %s) """
            cursor.execute(sql_insert_query, (name, contact, location, date, guests, time_selected))
            connection.commit()
            print("Record inserted successfully into bookings table")
            cursor.close()
    except Error as e:
        print("Failed to insert record into MySQL table {}".format(e))
    finally:
        if connection.is_connected():
            connection.close()


root = Tk()
root.title("Restaurant Table Booking System")
root.iconbitmap("table.ico")
root.geometry("600x400")
root.resizable(0, 0)
image_path = r"/Users/tsewangbista/Desktop/backend/F511855D-6DBD-4004-A4C4-CBABF487CFA2.jpeg"
image = Image.open(image_path)
image = image.resize((283, 600))  
bg_image = ImageTk.PhotoImage(image)

bg_label = Label(root, image=bg_image)
bg_label.pack(side="left", fill="y") 
root.config(bg="Dark cyan")

choices = ['12:00 PM', '12:30 PM', '1:00 PM', '1:30 PM', '2:00 PM', '2:30 PM', '3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', '6:00 PM', '6:30 PM', '7:00 PM', '7:30 PM', '8:00 PM', '8:30 PM', '9:00 PM', '9:30 PM', '10:00 PM', '10:30 PM', '11:00 PM', '11:30 PM']
time_dropdown =ttk.Combobox(root, values=["12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM", "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM", "9:30 PM", "10:00 PM", "10:30 PM", "11:00 PM", "11:30 PM"])
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


# Submit Button


submit_button = Button(root, text="DINE-IN", command=submit_data,bg= "Gray")
submit_button.place(x=400, y=350)
#added
dinein_button.bind("<Enter>", on_enter_dinein)
dinein_button.bind("<Leave>", on_leave_dinein)
admin_button.bind("<Enter>", on_enter_admin)
admin_button.bind("<Leave>", on_leave_admin)


dinein_button.grid(row=5, column=1, pady=20, padx=20)
admin_button.grid(row=5, column=2, pady=20, padx=20)
#//
#submit_login = Button(root, text="Login", command=login)

root.mainloop()

