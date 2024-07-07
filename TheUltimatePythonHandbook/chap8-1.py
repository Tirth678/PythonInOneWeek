# Write a program using functions to find greatest of three numbers.
def great(x1, x2, x3):
    if x1>x2:
        max = x1
    elif x2>x3:
        max = x2
    elif x3>x1:
        max = x3

    return max

print(great(69,2,3))