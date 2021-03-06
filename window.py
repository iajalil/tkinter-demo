# importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter
from tkinter import ttk

#create an instance of tk
window = tk.Tk()

# Giving out window a title
window.title( "our demo app" )

# restricting window resizing
window.resizable( True, True) #x and y

# introducing our first label
ttk.Label(window, text = "Guess my name"). grid(column =0, row = 0)
lblName =ttk.Label(window, text ="Guess my name")
lblName.grid(column=0, row = 0)

# Starting our buton up for an event
def reveal_me ():
    action.configure( text = "Mystery solved!") #Text that replaces "Guess my name"
    lblName.configure(foreground ="blue") #colour of the text
    lblName.configure(text = "Benjamin Benson") #name revealed

# starting up our textfield event
def click_me():
    text_action.configure( text = "hello " + name.get()) # Displaying user's name

#setting our text label
lblText = ttk.Label( window, text = "please enter a name" )
lblText.grid( column = 0, row = 2)

 #Adding the textbox widget
name = tk.StringVar ()
user_name = ttk.Entry ( window, width = 14, textvariable=name)
user_name.grid(column=0, row=3)
user_name.focus() # placing the cursor to focus on this texting

# Adding our button
action = ttk.Button(window, text="open sesame!", command=reveal_me) # Activating the button
action.grid(column=1, row =0 )
action.configure(state = "disabled") # Disabling the button

#Adding our text buton
text_action = ttk.Button(window, text = "click to greet" , command = click_me)
text_action.grid( column=1, row = 3)

# starting the GUI
window.mainloop()
