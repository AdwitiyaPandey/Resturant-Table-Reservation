from tkinter import*
import mysql.connector
from mysql.connector import Error

root = Tk()
root.title("Resturant Table Booking System")
root.iconbitmap("table.ico")
root.geometry("800x800")
root.resizable(0,0)

Label(root, text = "Dine Reserve", font = "Lobster 15 bold").pack()
Label(text="Name", font = "Garamond 10 bold").place(x=30, y=50)
Label(text="Contact", font = "Garamond 10 bold").place(x=30, y=90)
Label(text="Location,Resturant", font = "Garamond 10 bold").place(x=30, y=130)
Label(text="Date", font="Garamond 10 bold").place(x=30, y=170)
Label(text="Date", font="Garamond 10 bold").place(x=30, y=210)
Label(text="Guests", font="Garamond 10 bold").place(x=30, y=250)
e1 = Entry(root).place(x=150, y=50)
e2 = Entry(root).place(x=150, y=90)
e3 = Entry(root).place(x=150, y=130)
e4 = Entry(root).place(x=150, y=170)
e5 = Entry(root).place(x=150, y=210)
e6 = Entry(root).place(x=150, y=250)



root.mainloop()