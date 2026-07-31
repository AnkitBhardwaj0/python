"""
Answer below asked questions on given array:
1. Fetch Every alternate column of the array
2. Normalise the given array
"""
import numpy as np
a=np.random.randint(1,10000,40).reshape(8,5)
print(a,"\n")
print(a[:,::2])
normalization=(a-np.min(a))/(np.max(a)-np.min(a))
print(normalization)
print("\n",np.min(a))