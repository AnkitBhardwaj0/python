"""
Write a decorator which doubles the return value of any function. And test that decoratos is working correctly or not using `asert`
"""
def doubles(function):
    def wrapper(*args,**kwargs):
        return 2*function(*args,**kwargs)
        
    return wrapper
@doubles
def add(*args):
    return sum(args)

assert(add(5,2))==14
assert(add(1,2,3))==12
assert(add(10))==20
print("All tests passed!")