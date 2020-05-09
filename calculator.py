# simple calculator with 2 text fields,
# 4 buttons "+", "-", "*", "/"
# where user input numbers and
# the result of the calculation should be displayed in the label
# if input str - "Error" in the label

from tkinter import *

root = Tk()
root.title('Calculate')

# vidgets
entry_field1 = Entry(root, width=30)
entry_field2 = Entry(root, width=30)

plus_button     = Button(root, text="+")
minus_button    = Button(root, text="-")
multiply_button = Button(root, text="*")
division_button = Button(root, text="/")

result_label = Label(root, bg="black", fg="white", width=30)

# model

def calculate_sum(event):

    try:
        operand1 = int(entry_field1.get())
        operand2 = int(entry_field2.get())
        sum = operand1 + operand2
        result_label.config(text=int(sum))
    except:
        pass
        # String enter - Error

def calculate_minus(event):
    operand1 = int(entry_field1.get())
    operand2 = int(entry_field2.get())
    minus = operand1 - operand2
    result_label.config(text=int(minus))
    # String enter - Error
def calculate_multiply(event):
    operand1 = int(entry_field1.get())
    operand2 = int(entry_field2.get())
    multiply = operand1 * operand2
    result_label.config(text=int(multiply))
    # String enter - Error
def calculate_division(event):
    operand1 = int(entry_field1.get())
    operand2 = int(entry_field2.get())
    division = operand1 / operand2
    result_label.config(text=int(division))
    # division by Zero - Error
    # String enter - Error


plus_button.bind('<Button-1>', calculate_sum)
minus_button.bind('<Button-1>', calculate_minus)
multiply_button.bind('<Button-1>', calculate_multiply)
division_button.bind('<Button-1>', calculate_division)

#view
entry_field1.pack()
entry_field2.pack()
plus_button.pack()
minus_button.pack()
multiply_button.pack()
division_button.pack()
result_label.pack()

root.mainloop()