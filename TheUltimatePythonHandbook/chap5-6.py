# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

dict1 = {}
name = input("enter your name\n")
lang = input("input your language\n")
dict1.update({name: lang})
name = input("enter your name\n")
lang = input("input your language\n")
dict1.update({name: lang})
name = input("enter your name\n")
lang = input("input your language\n")
dict1.update({name: lang})
name = input("enter your name\n")
lang = input("input your language\n")
dict1.update({name: lang})
print(dict1)