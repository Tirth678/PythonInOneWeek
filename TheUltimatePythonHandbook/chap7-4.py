# Write a program to find whether a given number is prime or not
num = int(input("enter the value\n"))
if num%num == 0 and num%1 == 0 and num%4!=0:
    print("the number is a prime number\n")

else:
    print("the number is not a prime number\n")