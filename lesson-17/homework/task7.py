import matplotlib.pyplot as plt
import numpy as np
products=['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values=[200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'purple']
widths = [0.4, 0.6, 0.8, 1.0, 0.2]
plt.bar(products, values, color=colors, width=widths, edgecolor='black')
plt.title('Bar Chart')
plt.xlabel('Products')
plt.ylabel('Values')
plt.show()