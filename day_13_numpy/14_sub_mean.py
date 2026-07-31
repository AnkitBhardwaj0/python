#Subtract the mean of each row from a matrix.
import numpy as np
a=np.random.randint(1,100,20).reshape(4,5)
result=[]
for i in a:
    result.append( i-np.mean(i))

print(np.array(result))
