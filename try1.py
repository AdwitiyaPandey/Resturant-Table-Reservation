from tkinter import *
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk, Image
from tkinter import ttk

def submit_data():
    name = e1.get()
    contact = e2.get()
    location = e3.get()
    date = e4.get()  # Ensure this is in 'YYYY-MM-DD' format for MySQL
    guests = e5.get() #post()

    try: #learn more about try and except and finally
        connection = mysql.connector.connect(
            host='localhost',
            database='restaurant_booking',
            user='root',  # replace with your MySQL username
            password=''  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor() #learn more about cursor
            sql_insert_query = """ INSERT INTO bookings (name, contact, location, date, guests)
                                   VALUES (%s, %s, %s, %s, %s) """
            cursor.execute(sql_insert_query, (name, contact, location, date, guests))
            connection.commit()
            print("Record inserted successfully into bookings table")
            cursor.close()
    except Error as e:
        print("Failed to insert record into MySQL table {}".format(e))
    finally:
        if connection.is_connected():
            connection.close()

# Tkinter GUI setup
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




Label(root, text="Dine Reserve", font="Lobster 15 bold",bg= "Dark cyan").pack()
Label(text="Name", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=50)
Label(text="Contact", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=90)
Label(text="Location, Restaurant", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=130)
Label(text="Date (YYYY-MM-DD)", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=170)
Label(text="Time", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=210)
Label(text="Guests", font="Garamond 10 bold",bg= "Dark cyan").place(x=288, y=250)

e1 = Entry(root) #learn more about entry
e1.place(x=420, y=50)
e2 = Entry(root)
e2.place(x=420, y=90)
e3 = Entry(root)
e3.place(x=420, y=130)
e4 = Entry(root)
e4.place(x=420, y=170)
e5 = Entry(root)
e5.place(x=420, y=210)
e6 = Entry(root)
e6.place(x=420, y=250)

# Submit Button
submit_button = Button(root, text="DineIN", command=submit_data,bg= "Gray")
submit_button.place(x=400, y=300)
#submit_login = Button(root, text="Login", command=login)


root.mainloop()


