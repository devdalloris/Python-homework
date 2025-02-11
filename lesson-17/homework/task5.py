import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', alpha = 0.7, edgecolor='black')
plt.title('Basic Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()