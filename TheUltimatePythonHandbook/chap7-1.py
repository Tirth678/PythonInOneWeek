# Write a program to print multiplication table of a given number using for loop.
i = 0
n = int(input("enter the table you want\n"))
for i in range(11):
    print(f"{n}x{i}={n*(i+0)}")
    i = i+1