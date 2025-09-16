def decorator(func):
    def wrapper():
        print("Searching for your Girlfriend....")
        func()
        print("Hope you will get one soon....")
    return wrapper
def name():
    print("Sorry, Not applicable to you")
a = decorator(name)
a()
