"""
THIS IS A MINI - CALCULATOR APP THAT IS MEANT TO REGISTER MOUSE CLICKS AND KEYBOARD HITS 
"""

# Importing the tkinter module
from tkinter import *

class OurWindow:
    def __init__(self, win):
        # Setting up our labels
        self.lblFnum = Label( win, text = "First Number")
        self.lblFnum.place(x = 100, y = 50) # setting the position for First number label
        self.lblFSnum = Label( win, text = "Second Number")
        self.lblFSnum.place(x = 100 , y =100) # setting the position for Second number label
        self.lblResult = Label( win, text = "Result")
        self.lblResult.place(x = 100, y= 220) # setting the position for Result label

        # Setting up our Textboxes (Entry Fields)
        self.txtFnum = Entry()
        self.txtFnum.place (x = 200, y = 50) # Setting the position for the First Number entry field
        self.txtSnum = Entry()
        self.txtFnum.place (x = 200, y = 50) # Setting the position for the Second Number entry field
        self.txtSnum.place (x= 200, y= 100) 
        self.txtResult = Entry(bd = 5) # Giving the result textbox a border of width 5
        self.txtResult.place (x=200, y=220) # Setting the position for the result entry field

        # Setting up our Buttons
        self.btnAdd = Button( win, text = "Add", command = self.add )
        self.btnAdd.place (x = 100, y = 150) #Setting the position for the Add button
        self.btnSubtract = Button ( win, text = "Subtract", command = self.sub)
        self.btnSubtract.bind ("<Button-2>", self.sub)
        self.btnSubtract.place(x=150,y = 150) # Setting the position for the subtract
        self.btnmultiply = Button( win, text = "Multiply", command = self.multiply)
        self.btnmultiply.place (x = 220, y = 150)
        self.btndivide = Button( win, text = "divide", command = self.divide)
        self.btndivide.place (x = 300, y = 150)
        

    #Defining our addition event
    def add (self):
        self.txtResult.delete( 0, 'end')
        FirstNumber = int(self.txtFnum.get()) #Grabbing the input from the first number
        SecondNumber = int(self.txtSnum.get()) #Grabbing the input from the Second number

        Result = FirstNumber + SecondNumber #Performing the addition

        self.txtResult.insert (END, str( Result))

    #Defining our subtraction event
    def sub (self):
        self.txtResult.delete( 0, 'end')
        FirstNumber = int(self.txtFnum.get())#Grabbing the input from the first number
        SecondNumber = int(self.txtSnum.get())#Grabbing the input from the Second number

        result = FirstNumber - SecondNumber #Performing the subtraction


        self.txtResult.insert (END, str( result))
    
    #Defining our multiplication event
    def multiply (self):
        self.txtResult.delete(0, 'end')
        FirstNumber = int(self.txtFnum.get()) #
        SecondNumber = int(self.txtSnum.get())

        result = FirstNumber * SecondNumber

        self.txtResult.insert (END, str( result))

    #Defining our division event
    def divide (self):
        self.txtResult.delete(0, 'end')
        FirstNumber = int(self.txtFnum.get()) #
        SecondNumber = int(self.txtSnum.get())

        result = FirstNumber / SecondNumber

        self.txtResult.insert (END, str( result))

# Setting up the window
container = Tk()
myContainer = OurWindow(container)
container.title("Mini-Calculator")
container.geometry("500x400+10+10")
container.mainloop()