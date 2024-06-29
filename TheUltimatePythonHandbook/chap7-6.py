# Write a program to calculate the factorial of a given number using for loop.
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
    
num = 5
print("the factorial of the num is", factorial(num))