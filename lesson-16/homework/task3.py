import numpy as np
a=np.array([[4,3,2], [5, -1, 1], [6,1,-2]])
b=np.array([7,4,5])
x=np.linalg.solve(a,b)
print(x)