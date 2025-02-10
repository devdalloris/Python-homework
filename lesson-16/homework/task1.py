import numpy as np
far=np.array([32, 68, 100, 212, 77])

@np.vectorize
def far_to_cel(f):
    c=(f-32)*(5/9)
    return c

print(far_to_cel(far))