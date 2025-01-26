import numpy as np

# Create a 5x5 random matrix
random_matrix = np.random.random((5, 5))

# Normalize the matrix
normalized_matrix = (random_matrix - np.mean(random_matrix)) / np.std(random_matrix)

print("Random Matrix:")
print(random_matrix)
print("\nNormalized Matrix:")
print(normalized_matrix)