def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
             func(a)
        return wrapper
    return decorator

@repeat(108)
def shiv_mantra(a):
   print("ॐ नमः शिवाय")

shiv_mantra(None)