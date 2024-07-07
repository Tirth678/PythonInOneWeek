# Write a Python program to swap two variables
x = int(input("enter first variable\n"))
y = int(input("enter second variable\n"))
def swap(x, y):
    tend = x
    x = y
    y = tend

swap(x,y)
print(f"x and y after swap = {y} and {x}")