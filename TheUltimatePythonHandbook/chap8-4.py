def summation(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x+summation(x-1)
    
num = 5 #just for example
print(summation(num))