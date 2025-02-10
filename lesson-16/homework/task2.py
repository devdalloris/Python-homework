import numpy as np
a=np.array([2, 3, 4, 5])
b=np.array([1, 2, 3, 4])
@np.vectorize
def num_power(a,b):
    c=a**b
    return c
print(num_power(a,b))