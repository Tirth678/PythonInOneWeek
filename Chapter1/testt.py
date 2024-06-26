# def goodMorning(Name):
#     print(Name   + "  Good Morning!")



# goodMorning("Kedaar")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

num = 5
factorial(num)
print(factorial(num))