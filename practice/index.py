x = int(input("Enter your age\n"))
if x < 18:
    print("You are not eligible to vote\n")
elif x == 18:
    print("You're eligible to vote\n")
elif x > 18:
    print("You are eligible to vote\n")
else:
    print("Invalid user input\n")