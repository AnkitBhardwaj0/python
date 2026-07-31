"""
Elements count
Count the number of elements of a numpy array.
"""
import numpy as np
def element_count(ar):
    count=0
    for _ in ar:
        count+=1
    return count

print(element_count(np.array([])))
def e_count(arr):
    return arr.size
print(e_count(np.array([])))