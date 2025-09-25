import os


# Check if the folder exists before listing its contents
if os.path.exists("free folder"):
    a = os.listdir("free folder")
    print(a)
else:
    print("The folder 'free folder' does not exist.")

# Print the current working directory
print(os.getcwd())

# Check if the file exists before performing operations
if os.path.exists("sample.txt"):
    print("The file 'sample.txt' exists.")
    # Uncomment the following line to remove the file
    # os.remove("sample.txt")
else:
    print("The file 'sample.txt' does not exist.")

# Check if the folder exists before attempting to remove it
if os.path.exists("free folder"):
    # Uncomment the following line to remove the folder
    # os.rmdir("free folder")
    pass