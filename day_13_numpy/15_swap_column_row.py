#Swap column-1 of array with column-2 in the array. 
import numpy as np
a=np.random.randint(1,100,20).reshape(4,5)
print(a,"\n")
result=[]
for i in a.T:
    result.append(i)

result[0],result[1]=result[1],result[0]
print(np.array(result).T)

#method 2
a[:, [0, 1]] = a[:, [1, 0]]

print("\nAfter swapping:")
print(a)