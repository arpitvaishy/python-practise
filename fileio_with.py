with open("text.txt", "r") as file:
    content = file.read()   
print(content)
# when we use 'with' it automatically closes the file so we don't need to write file.close() or whatever the name