from tkinter import*
root=Tk()
root.title("Facebook")
root.geometry("500x500")
root.resizable(0,0)
name = Label(root, text = "Name").place(x=30, y=50)
address = Label(root, text = "Address").place(x=30, y=90)
e1 = Entry(root).place(x=80, y=50)
e2 = Entry(root).place(x=80, y=90)

Button(root,text="Login",bg="black",fg="white").pack()
Button(root,text="Sign Up",bg="black",fg="white").pack()


mainloop()
