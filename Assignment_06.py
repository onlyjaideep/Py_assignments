#Using the Math Module for Calculations
import math
# Get user input for the number
def arithematic(num):
    if num == 0:
        print("sine value of zero is zero.")
        print("Cannot perform logarithm and exponential operations on zero.")
        return
    else:
        square_root = math.sqrt(num)
        natural_log = math.log(num)
        sine_value = math.sin(num)

        print(f"Square root of {num} is {square_root}")
        print(f"Logarithm of {num} is {natural_log}")
        print(f"sine value of {num} is {sine_value}")
n = float(input("Enter a number to perform arithematic operations: "))
arithematic(n)