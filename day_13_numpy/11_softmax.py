#Softmax function
import numpy as np
def softmax_function(z):
    return np.exp(z)/np.sum(np.exp(z))

z=np.array([1,2,3,4,5])
print(softmax_function(z))