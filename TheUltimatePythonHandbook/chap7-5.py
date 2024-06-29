# Write a program to find the sum of first n natural numbers using while loop.
def summation(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x+summation(x-1)
num = 5
print(summation(num))