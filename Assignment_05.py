# Calculate Factorial Using a Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1) 
    
# Get user input for the number
n = int(input("Enter an integer to calculate its factorial: "))
print(f"Factorial of {n} is {factorial(n)}")