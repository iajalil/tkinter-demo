#importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter
from tkinter import ttk

win = tk.Tk()

#Giving the window a title
win.title('customer sign up form')

#creating an empty space
ttk.label(win).grid(row=0)

#Setting our username labels and input boxes
lblUserName = ttk.Label (win, text = "Username:")
lblUserName.grid(column=1 , row= 1)

#creating an empty space
ttk.Label(win).grid (row=2)

#setting or username textbox
name=tk.StringVar()
txtUsername = ttk.Entry(win, width= 16, textvariable = name) 
txtUsername.grid(column =3, row =1)

#setting our email labels and input boxes
lblEmail = ttk.Label(win,text = "Email: ")
lblEmail.grid(column=1, row=3)

#setting our email textbox
email = tk.StringVar()
txtEmail = ttk.Entry(win, width=25, textvariable= email)
txtEmail.grid(column=3, row=3)

#creating an empty space
ttk.Label(win).grid(row=4)

#setting our password labels and input boxes
lblPassword = tk.Label(win, textvariable="Password")
lblPassword.grid(column=1, row=5)

#setting our password text box
password = tk.StringVar()
txtPassword =ttk.Entry(win, width=20, textvariable=password)
txtPassword.grid(column=3, row=5)

#Creating an empty space
tk.Label(win).grid(row=6)

#setting up our submit button
btnSubmit =ttk.Button(win, width= 15, text="submit ")
btnSubmit.grid(column=3, row=7)

#Invoking our GUI loop
win.mainloop()