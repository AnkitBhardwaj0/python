"""
Generator time elapsed
Write a generator function whose argument must be iterable. With each iteration, the generator will return a two-element tuple. The first element in the tuple will be an integer indicating how many seconds have passed since the previous iteration. The tuple’s second element will be the next item from the passed argument.
"""
import time
def gen(strings):
    previous_time=None
    for i in strings:
        current_time=time.time()
        if previous_time is None:
            elapsed_time = 0.0
        else:
            elapsed_time=current_time - previous_time
        yield (elapsed_time, i)
        previous_time=current_time
        

for i in gen("abcdef"):
    print(i)
    time.sleep(2)