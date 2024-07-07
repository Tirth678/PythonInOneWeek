# Write a Python Program to Print the Fibonacci sequence
def femonachi(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return femonachi(x-1)+femonachi(x-2)

num = 0
while(num<10):
        print(femonachi(num))
        num = num+1