# Importing our tkinter module
from tkinter import *
from tkinter import ttk #importing the ttk class
from tkinter.messagebox import showinfo

# Setting up our window
win = Tk()
win.geometry ("400x350")
win.title("My Login System")

def message():
    if len(strVar1.get()) !=0 and len(strVar2.get()) !=0:
        showinfo( "Message", f"You are successfully logged in!")
    else:
        showinfo( "Message", f"Please enter the correct username and password")

# Design our username
lblUsername = Label(win, text = "Username", font = ( "Arial Bold", 15))
lblUsername.place(x = 50, y = 50)

# Design username text field
strVar1 = StringVar()
txtUsername = Entry( win, width = 20 , textvariable=strVar1)
txtUsername.place(x =170, y = 57)

# Designing our password label
lblPassword= Label (win, text = "Password", font = ( "Arial Bold" , 15))
lblPassword.place(x=50, y = 100)

# Desining our password text field
strVar2=StringVar()
txtPassword=Entry(win, width=20, textvariable= strVar2)
txtPassword.place (x = 170, y = 100)

# Designing our login Button
btnLogin = Button (win, text = "Login", width=20, command = message)
btnLogin.place(x=100, y = 150)


















win.mainloop()