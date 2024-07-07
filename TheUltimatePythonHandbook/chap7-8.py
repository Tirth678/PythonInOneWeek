# Write a program to print the following star pattern:
# *
# **
# *** for n = 3
i = 0
n = int(input("enter the value\n"))
for i in range(i, n+1):
    print("*"*i, end = "")
    print("")
