# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
bio = int(input("enter the marks of biology\n"))
eng = int(input("enter the marks of english\n"))
maths = int(input("enter the marks of maths\n"))

if (bio +eng +maths)/3>=40 and bio>=33 and eng>=33 and maths>=33:
    print("passed\n")
else:
    print("failed\n")