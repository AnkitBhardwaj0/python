"""
You are given a space separated list of numbers. Your task is to print a reversed NumPy array with the element type float.

"""
import numpy as np
number=np.array(list(map(int,input().split())))
print(number)
number=number.astype(float)
print(number[::-1])