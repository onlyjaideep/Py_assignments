from tkinter import *

# Interface -----------------------------------------------------
window = Tk()
window.title("Simple Calculator")
window.geometry("400x400")

# Functions for button clicks -----------------------------------
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    try:
        expression = e.get()
        result = eval(expression) # Simple way for beginners to calculate strings
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Entry box -----------------------------------------------------
e = Entry(window, width=60, borderwidth=5)
e.place(x=0, y=0)

# Buttons -------------------------------------------------------
# Row 1
b1 = Button(window, text='1', width=12, height=2, command=lambda: button_click(1))
b1.place(x=10, y=60)

b2 = Button(window, text='2', width=12, height=2, command=lambda: button_click(2))
b2.place(x=90, y=60)

b3 = Button(window, text='3', width=12, height=2, command=lambda: button_click(3))
b3.place(x=180, y=60)

b_clear = Button(window, text='Clear', width=12, height=2, command=button_clear)
b_clear.place(x=270, y=60)

# Row 2
b4 = Button(window, text='4', width=12, height=2, command=lambda: button_click(4))
b4.place(x=10, y=120)

b5 = Button(window, text='5', width=12, height=2, command=lambda: button_click(5))
b5.place(x=90, y=120)

b6 = Button(window, text='6', width=12, height=2, command=lambda: button_click(6))
b6.place(x=180, y=120)

b_add = Button(window, text='+', width=12, height=2, command=lambda: button_click('+'))
b_add.place(x=270, y=120)

# Row 3
b7 = Button(window, text='7', width=12, height=2, command=lambda: button_click(7))
b7.place(x=10, y=180)

b8 = Button(window, text='8', width=12, height=2, command=lambda: button_click(8))
b8.place(x=90, y=180)

b9 = Button(window, text='9', width=12, height=2, command=lambda: button_click(9))
b9.place(x=180, y=180)

b_sub = Button(window, text='-', width=12, height=2, command=lambda: button_click('-'))
b_sub.place(x=270, y=180)

# Row 4
b_dot = Button(window, text='.', width=12, height=2, command=lambda: button_click('.'))
b_dot.place(x=10, y=240)

b0 = Button(window, text='0', width=12, height=2, command=lambda: button_click(0))
b0.place(x=90, y=240)

# FIXED: Removed lambda and ('=') because button_equal doesn't take arguments
b_equal_btn = Button(window, text='=', width=12, height=2, command=button_equal)
b_equal_btn.place(x=180, y=240)

b_mul = Button(window, text='*', width=12, height=2, command=lambda: button_click('*'))
b_mul.place(x=270, y=240)

window.mainloop()