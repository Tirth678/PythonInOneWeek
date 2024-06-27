# a group of statements which performs a specific task.
# def func1():
#     print("Hello\n")


# func1()

# def greet(name = "lol"):
#     print("Good day " + name)

    # result = "Good day " + name
    # return result 


# greet()
# greet("dhruv")

def factorial(x):
    if x == 1 or x == 0:
        return 1
    
    else:
        return x*factorial(x-1)
    
num = 5
print(factorial(num))