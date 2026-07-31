"""Consider a random integer (in range 1 to 100) vector with shape `(10,2)` representing coordinates, and coordinates of a point as array is given. Create an array of distance of each point in the random vectros from the given point. Distance array should be interger type."""
import numpy as np
def distance(point):
    a = np.random.randint(1, 101, size=(10,2))
    dist=np.zeros(10)
    for i in range(len(a)):
        dist[i]=np.sqrt((a[i,0]-point[0])**2+(a[i,1]-point[1])**2)
    return dist


x = int(input("Enter x: "))
y = int(input("Enter y: "))
point = np.array([x, y])
print(distance(point))