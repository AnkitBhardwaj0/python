"""
Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.
"""
from encodings import cp500

import numpy as np
import random

a=int(input("enter a number "))
b=int(input("enter a number "))
c=np.random.random((a,b))*100
c=np.round(c)
print(c)
print(np.mean(c))