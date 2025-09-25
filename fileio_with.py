with open("text.txt", "r") as file: #context manager
    content = file.read()   
print(content)
# when we use 'with' syntax it automatically closes the file so we don't need to write file.close() or whatever the name