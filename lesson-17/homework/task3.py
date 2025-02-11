import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
y1=x**3
y2=np.sin(x)
y3=np.e**x
y4=np.log(x+1)
fig, axes = plt.subplots(2, 2)  # 2x2 grid of subplots
axes[0, 0].plot(y1, c='r', linestyle='--', marker='s', label='y1=sin(x)')  # Top-left subplot
axes[0, 1].plot(y2, c='g', linestyle='-.', marker='o', label='y2=sin(x)')  # Top-right subplot
axes[1, 0].plot(y3, c='b', linestyle='-', marker='v', label='y3=e**x')  # Bottom-left subplot
axes[1, 1].plot(y4, c='y', linestyle=':', marker='D', label='y1=log(x+1)')  # Bottom-right subplot
axes[0, 0].legend()
axes[0, 1].legend()
axes[1, 0].legend()
axes[1, 1].legend()
axes[0, 0].set_title('First function')
axes[0, 1].set_title('Second function')
axes[1, 0].set_title('Third function')
axes[1, 1].set_title('Fourth function')
plt.show()