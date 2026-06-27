from tkinter import *

# Interface -----------------------------------------------------
window = Tk()
window.title("Simple Calculator")
window.geometry("400x400")

# Functions for button clicks -----------------------------------
def button_click(number):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(number))

def button_clear():
    e.delete(0, END)

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

# Operators
def button_add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    # CHANGED: Using float() so your decimal button doesn't crash the code
    i = float(n1)
    e.delete(0, END)

# FIXED: Changed command to call button_add directly instead of button_click('+')
b_add = Button(window, text='+', width=12, height=2, command=button_add)
b_add.place(x=270, y=120)

# Row 3
b7 = Button(window, text='7', width=12, height=2, command=lambda: button_click(7))
b7.place(x=10, y=180)

b8 = Button(window, text='8', width=12, height=2, command=lambda: button_click(8))
b8.place(x=90, y=180)

b9 = Button(window, text='9', width=12, height=2, command=lambda: button_click(9))
b9.place(x=180, y=180)

# Operators
def button_sub():
    n1 = e.get()
    global math
    math = 'subtraction'
    global i
    i = float(n1)
    e.delete(0, END)

# FIXED: Changed command to call button_sub directly
b_sub = Button(window, text='-', width=12, height=2, command=button_sub)
b_sub.place(x=270, y=180)

# Row 4
b_dot = Button(window, text='.', width=12, height=2, command=lambda: button_click('.'))
b_dot.place(x=10, y=240)

b0 = Button(window, text='0', width=12, height=2, command=lambda: button_click(0))
b0.place(x=90, y=240)

# Operators
def button_equal():
    n2 = e.get()
    e.delete(0, END)
    
    # FIXED: Changed int(n2) to float(n2) to match standard math outputs
    if math == 'addition':
        ans = i + float(n2)
    elif math == 'subtraction':
        ans = i - float(n2)
    elif math == 'multiplication':
        ans = i * float(n2)
    
    # Clean up output: drops '.0' if it's a whole number
    if ans.is_integer():
        e.insert(0, int(ans))
    else:
        e.insert(0, ans)

b_equal_btn = Button(window, text='=', width=12, height=2, command=button_equal)
b_equal_btn.place(x=180, y=240)

# Operators
def button_mul():
    n1 = e.get()
    global math
    math = 'multiplication'
    global i
    i = float(n1)
    e.delete(0, END)

# FIXED: Changed command to call button_mul directly
b_mul = Button(window, text='*', width=12, height=2, command=button_mul)
b_mul.place(x=270, y=240)

window.mainloop()