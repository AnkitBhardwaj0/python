"""
Given two arrays of same shape make an array of max out of two arrays. (Numpy way)
"""
import numpy as np
a=np.random.randint(1,100,15).reshape(3,5)
b=np.random.randint(1,100,15).reshape(3,5)
print(a,"\n")
print(b,"\n")
result=np.maximum(a,b)

print(result)