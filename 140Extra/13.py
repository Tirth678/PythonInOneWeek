# Write a Python Program to Check Leap Year.
year = int(input("enter the year\n"))
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print("the year is a leap year\n")

else:
    print("the year is not a leap year\n")