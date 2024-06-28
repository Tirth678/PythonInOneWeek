# Write a program to find the greatest of four numbers entered by the user
num1 = int(input("enter the value 1\n"))
num2 = int(input("enter the value 2\n"))
num3 = int(input("enter the value 3\n"))
num4 = int(input("enter the value 4\n"))

if num1>num2:
    max = num1
elif num2>num3:
    max = num2
elif num3>num4:
    max = num3
elif num4>num1:
    max = num4
print("the max value among the following is", max)