from tkinter import *
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox, ttk
from datetime import datetime


def submit_data():
    name = e1.get()
    contact = e2.get()
    location = location_dropdown.get()
    date = e4.get()  
    guests = e6.get() 
    time_selected = time_dropdown.get()
     
    if not name or not contact or not location or not date or not guests or not time_selected:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    try: 
        connection = mysql.connector.connect(
            host='localhost',
            database='restaurant_booking',
            user='root',  
            password=''  
        )

        if connection.is_connected():
            cursor = connection.cursor() 
            sql_insert_query = """ INSERT INTO bookings (name, contact, location, guests, time1, date)
                                   VALUES (%s, %s, %s, %s, %s, %s) """
            cursor.execute(sql_insert_query, (name, contact, location, guests, time_selected, date))
            connection.commit()
            print("Record inserted successfully into bookings table")
            cursor.close()
            messagebox.showinfo("Success", "Booking Successful!")
    except Error as e:
        print("Failed to insert record into MySQL table {}".format(e))
    finally:
        if connection.is_connected():
            connection.close()

def open_admin_login(): 

    admin_window = Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.geometry("300x150")
    admin_window.grab_set()
    

    Label(admin_window, text="Username:").pack(pady=5)
    admin_name_entry = Entry(admin_window)
    admin_name_entry.pack()
    
    Label(admin_window, text="Password:").pack(pady=5)
    admin_uid_entry = Entry(admin_window, show="*")  
    admin_uid_entry.pack()

    def verify_admin():  
        input_name = admin_name_entry.get()
        input_uid = admin_uid_entry.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='admin',
                user='root',
                password=''
            )

            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM login WHERE name = %s AND uid = %s", 
                               (input_name, input_uid))
                result = cursor.fetchone()

                if result:
                    messagebox.showinfo("Success", "Login Successful!")
                    admin_window.destroy()
                    show_reservations(input_name)  
                else:
                    messagebox.showerror("Error", "Invalid Credentials")
                cursor.close()

        except Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if connection.is_connected():
                connection.close()
    
    Button(admin_window,text="Log-in", command=verify_admin).pack(pady=10)


def show_reservations(restaurant_name):
  
    reservations_window = Toplevel(root)
    reservations_window.title(f"{restaurant_name} Reservations")
    reservations_window.geometry("800x400")

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='restaurant_booking',
            user='root',
            password=''
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM bookings WHERE location = %s", (restaurant_name,))
            reservations = cursor.fetchall()

            columns = ("ID", "Name", "Contact", "Location", "Guests", "Time", "Date")
            tree = ttk.Treeview(reservations_window, columns=columns, show="headings")

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100, anchor="center")

            for res in reservations:
                tree.insert("", "end", values=res)

            tree.pack(expand=True, fill="both")

            cursor.close()

    except Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        if connection.is_connected():
            connection.close()


def fetch_locations():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="admin"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM login")  
            locations = [row[0] for row in cursor.fetchall()] 
            cursor.close()
            connection.close()
            return locations
    except Error as e:
        print(f"Error fetching locations: {e}")
        return []


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




locations = fetch_locations()  
location_dropdown = ttk.Combobox(root, values=locations)
location_dropdown.place(x=420, y=130)


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
e4 = Entry(root)
e4.place(x=420, y=170)
e6 = Entry(root)
e6.place(x=420, y=250)


submit_button = Button(root, text="DINE-IN", command=submit_data,bg= "Gray")
submit_button.place(x=400, y=350)
submit_button2 = Button(root, text="ADMIN", command=open_admin_login, bg="Gray")
submit_button2.place(x=500, y=350)

root.mainloop()
