# importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter
from tkinter import ttk

#create an instance of tk
window = tk.Tk()

# Giving out window a title
window.title( "our demo app" )

# restricting window resizing
window.resizable( True, True)

# introducing our first label
ttk.Label(window, text = "Guess my name"). grid(column =0, row = 0)
lblName =ttk.Label(window, text ="Guess my name")
lblName.grid(column=0, row = 0)

# Starting our buton up for an event
def reveal_me():
    action.configure( text = "Mystery solved") #Text that replaces "Guess my name"
    lblName.configure(foreground ="blue") #colour of the text
    lblName.configure(text = "Benjamin Benson") #name revealed

# Adding our button
action = ttk. Button( window, text = "open Sesame!", command = reveal_me) #Activating the button
action.grid( column = 1, row = 0)

# starting the GUI
window.mainloop()