import matplotlib.pyplot as plt
import numpy as np
a = np.arange(100)
b = np.random.randint(0, 100, 100)
sizes = np.abs(np.random.randn(100)) * 100
plt.title('Function')
plt.xlabel('Range of x')
plt.ylabel('Range of y')
plt.scatter(a, b, s=sizes, c=b, cmap='cool')
plt.colorbar()
plt.show()