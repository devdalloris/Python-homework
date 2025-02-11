import matplotlib.pyplot as plt
import numpy as np
categories = ['Category A', 'Category B', 'Category C']
t1 = [10, 15, 7]
t2 = [5, 10, 3]
t3 = [2, 16, 1]
plt.bar(categories, t1, label='Dataset 1', color='blue')
plt.bar(categories, t2, label='Dataset 2', color='green')
plt.bar(categories, t3, label='Dataset 3', color='red')
plt.title('Stacked Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()