import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 2*np.pi)
print(x)
y1=np.sin(x)
y2=np.cos(x)
plt.title('Function y1=sin(x) and y2=cos(x)')
plt.xlabel('Range of x')
plt.ylabel('Range of y')
plt.plot(x,y1, c='r', linestyle='--', marker='s', label='y1=sin(x)')
plt.plot(x,y2, c='g', linestyle='-.', marker='*', label='y2=cos(x)')
plt.legend()
plt.show()