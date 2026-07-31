"""
Vertical stack
Write a python function that accepts infinite number of numpy arrays and do the vertical stack to them. Then return that new array as result. The function only accepts the numpy array, otherwise raise error.
"""
import numpy as np
def vertical_stack(*arrays):
    for array in arrays:
        if not isinstance(array,np.ndarray):
            raise (f"{array} must be numpy arrays. \n")
    
    return np.vstack(arrays)
        
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
arr4 = np.arange(12).reshape(4,3)
arr6 = np.arange(3)

result = vertical_stack(arr1,arr2,arr3,arr4,arr6
)

print(result)    