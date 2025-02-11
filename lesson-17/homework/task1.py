import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10, 11)
y=x**2-4*x+4
print(x)
plt.title('Function f(x)=y=x**2-4*x+4')
plt.xlabel('Range of x')
plt.ylabel('Range of y')
plt.plot(x,y)
plt.show()