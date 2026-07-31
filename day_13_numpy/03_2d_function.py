#Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.
import numpy as np
import numpy as np

def arr(a, b):
    ar = np.zeros((a, b), dtype=int)
    ar[0, :] = 1   
    ar[-1, :] = 1     
    ar[:, 0] = 1      
    ar[:, -1] = 1     
    return ar
print(arr(3,4))