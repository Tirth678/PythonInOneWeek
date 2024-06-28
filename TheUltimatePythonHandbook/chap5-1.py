# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

meaning = {"stop": "ruko",
           "start": "shuru",
           "move": "chalo"}
result = meaning.get("stop")
print(result)