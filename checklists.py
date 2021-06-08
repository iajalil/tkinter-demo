# importing our tkinter module
from tkinter import *
from tkinter.ttk import Combobox #Importing Combobox

# creating an instance of Tk window
win = Tk()

numbers = ( "One", "Five", "Eleven", "Twelve" , "Sixteen") 

# creating our listbox
lbListbox = Listbox(win,  height=5, selectmode = "multip9le")

#Looping through the numbers one by one to be used in the listbox
for number in numbers:
    lbListbox.insert(END, number ) # Insert every number at the end( on the next line)
lbListbox.place(x=250, y = 150)

#Creating our Combobox
data = StringVar() # Variable to record selections or inputs
data.set(numbers[0]) #Taking the first value in the numberrs tuple variable

cbCombobox = Combobox( win, value = numbers) #Setting the values for combobox
cbCombobox.place(x = 60, y =150)



#creating a checkbutton
check1_value =IntVar() # Creating a variable to hold integer values
Check2_value = IntVar() # Creating a variable to hold integer values
cb1Checkbox =  Checkbutton( win, text = "Guava" , variable = check1_value)
cb2Checkbox = Checkbutton (win, text = "Orange" , variable = Check2_value)

cb1Checkbox.place(x =70, y = 100) #Position for first Checkbutton
cb2Checkbox.place(x = 130, y =100) #Position for second Checkbutton

#Creating a radiobutton
rb_value = IntVar()
rb_value.set( 1 )

rb1_Radiobutton = Radiobutton(win, text ="Male", variable=rb_value, value=1)
rb2_Radiobutton = Radiobutton(win, text ="Female", variable=rb_value, value=2)
rb1_Radiobutton.place(x =70, y =50) #position for 1st radiobutton
rb2_Radiobutton.place(x =130, y =50) #position for 2nd  radiobutton

win.title( "Checklist App")
win.geometry( "400x300+10+10")
win.mainloop()