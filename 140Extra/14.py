# Write a Python Program to Check Prime Number
x = int(input("enter number\n"))
if x%x == 0 and x%1 ==0 and x%2!=0 or x == 2:
    print("the number is prime\n")

else:
    print("the number is not prime\n")