"""
 Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.
 """
def decor(function):
    def wrapper(*args,**kwargs):
        function(*args,**kwargs)
        function(*args,**kwargs)
    return wrapper
@decor
def greet(strings):
    print(strings)

greet("ankit")

