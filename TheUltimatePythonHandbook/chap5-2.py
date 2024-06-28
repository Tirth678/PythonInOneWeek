unique=[]
for i in range(9): 
   a=input("enter no.")
   if a not in unique: # add this line
      unique.append(a)
print(unique)