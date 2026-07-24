"""
Write a decorator called `printer` which causes any decorated function to print their return values. If the return value of a given function is `None`, printer should do nothing.
"""
def printer(function):
    def wrapper(*args, **kwargs):
        result=function(*args, **kwargs)
        print("Decorator started")
        if result is not None:
            print("Decorator prints:",result)
        return result
    return wrapper
@printer
def greet():
    print("hi ! how are you")
    return None
@printer
def greet1():
    print("hi ! how are you")
    
@printer
def greet2():
    return "hi ! how are you"

greet() 
greet1()
greet2()
    