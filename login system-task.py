# Importing our tkinter module
from tkinter import *
from tkinter import ttk #importing the ttk class
from tkinter.messagebox import showinfo

# Setting up our window
win = Tk()
win.geometry ("400x350")
win.title("My Login System")

def message():
    if len(strVar1.get()) !=0 and len(strVar2.get()) !=0 and len(strVar3.get() ) !=0 and len(strVar4.get() ) !=0:
        showinfo( "Message", f"You are successfully logged in!")
    else:
        showinfo( "Message", f"Please enter the correct username , email, telephone and password")

# Design our username
lblUsername = Label(win, text = "Username", font = ( "Arial Bold", 15))
lblUsername.place(x = 50, y = 50)

# Design username text field
strVar1 = StringVar()
txtUsername = Entry( win, width = 20 , textvariable=strVar1)
txtUsername.place(x =170, y = 50)

# Designing our Email label
lblEmail= Label (win, text = "Email", font = ( "Arial Bold" , 15))
lblEmail.place(x=50, y = 100)

# Desining our Email text field
strVar2=StringVar()
txtEmail=Entry(win, width=20, textvariable= strVar2)
txtEmail.place (x = 170, y = 100)

# Designing our telephone number button
lblTelephone = Label (win, text = "Telephone", font = ( "Arial Bold" , 15))
lblTelephone.place(x=50, y = 150)

# Desining our Telephone Number text field
strVar3=StringVar()
txtPassword=Entry(win, width=20, textvariable= strVar3)
txtPassword.place (x = 170, y = 150)

# Designing our password label
lblPassword= Label (win, text = "Password", font = ( "Arial Bold" , 15))
lblPassword.place(x=50, y = 200)

# Desining our password text field
strVar4=StringVar()
txtPassword=Entry(win, width=20, textvariable= strVar4)
txtPassword.place (x = 170, y = 200)


# Designing our login Button
btnLogin = Button (win, text = "Login", width=20, command = message)
btnLogin.place(x=100, y = 250)














win.mainloop()