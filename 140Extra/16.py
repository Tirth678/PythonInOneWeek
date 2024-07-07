# Write a Python Program to Find the Factorial of a Number.
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
    
num = (int(input("enter the value\n")))
print(factorial(num))