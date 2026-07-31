"""
Write a function which will accept 2 arguments.
First: A 1D numpy array arr
Second: An integer n {Please make sure n<=len(arr)}
"""
import numpy as np
def fun(arr,n):
    if not isinstance(arr, np.ndarray): 
        raise TypeError( "arr must be a NumPy array." )

    if arr.ndim != 1: 
        raise ValueError( "arr must be a 1D NumPy array." )
    if not isinstance(n, int): raise TypeError( "n must be an integer." )

    if not len(arr)>=n >=1:
        raise ValueError (f"{n} is greater than length of array")
    else:  
        arr=np.sort(arr)[::-1]
        return arr[n-1],arr

arr=np.random.randint(1,100,np.random.randint(1,100))
print(arr,"\n")
n=int(input(f"enter the number less than an equal to {len(arr)} : "))
result,arr=fun(arr,n)
print(arr,"\n")
print(result)
