"""
Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
"""
"""
Shape = (6, 7, 8)This means:

6 blocks
Each block has 7 rows
Each row has 8 columns
So each block contains:
7 × 8 = 56 elements

The 100th element (assuming 1-based counting, as the question states) corresponds to index:
100 - 1 = 99
99 ÷ 56 = 1 remainder 43
x = 1
43 ÷ 8 = 5 remainder 3
y = 5
z = 3
answer:-index =[1,5,3]
"""
import numpy as np

a = np.arange(6 * 7 * 8).reshape(6, 7, 8)
print(np.unravel_index(99, a.shape))