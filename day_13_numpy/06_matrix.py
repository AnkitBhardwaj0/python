#Create a 5x5 matrix with row values ranging from 0 to 4.

from sqlite3 import Row

import numpy as np
a=np.zeros((5,5))
for i in range(0,5):
    a[i]=i
print(a,"\n")

b = np.arange(5).reshape(5, 1)
b = np.broadcast_to(b, (5, 5))

print(b)