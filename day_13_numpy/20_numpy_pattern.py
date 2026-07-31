"""
Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])"""
import numpy as np
a = np.array([1,2,3])
a=np.hstack((np.ones(3),np.full(3,2),np.full(3,3),a,a,a))
print(a)

#advanced
a = np.array([1,2,3])
result = np.hstack((
    np.repeat(a, len(a)),
    np.tile(a, len(a))
))