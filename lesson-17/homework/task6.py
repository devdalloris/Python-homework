import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
xx, yy = np.meshgrid(x, y)
zz = np.cos(xx**2 + yy**2)
ax.plot_surface(xx, yy, zz, cmap='viridis')
plt.show()