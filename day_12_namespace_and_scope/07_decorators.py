"""
Write a Python program to make a chain of function decorators (bold, italic, underline etc.) on a given function which prints "hello world"
"""
"""
"**Hello**"      # Bold
"*Hello*"        # Italic
"***Hello***"    # Bold + Italic
"""
def bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper
def italic(function):
    def wrapper():
        return f"<i>{function()}</i>"
    return wrapper
def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper
@bold
@italic
@underline
def greet():
    return("Hello Ankit")

print(greet())