#Replace odd elements in arrays with -1.
import numpy as np
a=np.random.randint(1,100,20).reshape(5,4)
a=np.where(a%2!=0,-1,a)
print(a)