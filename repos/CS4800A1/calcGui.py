import calc
from tkinter import *

#Create scene for calculator
root = Tk()
root.title("Calculator")

#Space for calculations to be done
box = Entry(root, width=46, borderwidth=5)
box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Event handlers
#Enters the button input for equations
def button_click(selection):
    insert_point = box.get()
    box.delete(0, END)
    box.insert(0, str(insert_point) + str(selection))
    
#Evaluates entry box
def button_equals():
    equation = box.get()
    answer = eval(equation)
    box.delete(0, END)
    box.insert(0, str(answer))

#Empties the entry box
def button_clear():
    box.delete(0, END)

#Create buttons
num1 = Button(
    root,
    text="1",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(1)
)
num2 = Button(
    root,
    text = "2",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(2)
)
num3 = Button(
    root,
    text = "3",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(3)
)
num4 = Button(
    root,
    text = "4",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(4)
)
num5 = Button(
    root,
    text = "5",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(5)
)
num6 = Button(
    root,
    text = "6",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(6)
)
num7 = Button(
    root,
    text = "7",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(7)
)
num8 = Button(
    root,
    text = "8",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(8)
)
num9 = Button(
    root,
    text = "9",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(9)
)
num0 = Button(
    root,
    text = "0",
    padx=89,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click(0)
)
decimal = Button(
    root,
    text = ". ",
    padx=40,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click('.')
)
equal = Button(
    root,
    text="=",
    padx=79,
    pady=20,
    bg = "gray",
    fg = "black",
    command=button_equals
)
add = Button(
    root,
    text="+",
    padx=28.5,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click('+')
)
subtract = Button(
    root,
    text="-",
    padx=30,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click('-')
)
multiply = Button(
    root,
    text="*",
    padx=30,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click('*')
)
divide = Button(
    root,
    text="/",
    padx=30,
    pady=20,
    bg = "gray",
    fg = "black",
    command=lambda: button_click('/')
)
clear = Button(
    root,
    text="Clear",
    padx=78.5,
    pady=20,
    bg="gray",
    fg='black',
    command=lambda: button_clear()
)

#Organizing buttons into the grid
num1.grid(row=3, column=0)
num2.grid(row=3, column=1)
num3.grid(row=3, column=2)
subtract.grid(row=3, column=3)

num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)
multiply.grid(row=2, column=3)

num7.grid(row=1, column=0)
num8.grid(row=1, column=1)
num9.grid(row=1, column=2)
divide.grid(row=1, column=3)

num0.grid(row=4, column=0, columnspan=2)
decimal.grid(row=4, column=2)
add.grid(row=4, column=3)

equal.grid(row=5, column=2, columnspan=2)
clear.grid(row=5, column=0, columnspan=2)

#Loop the program
root.mainloop()