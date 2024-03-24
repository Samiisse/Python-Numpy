#Given a NumPy array, calculate the dot product of the array with itself

import numpy as np

# Given NumPy array
array = np.array([1, 2, 3])

# Calculate the dot product of the array with itself
dot_product = np.dot(array, array)
# Alternatively, you can use the @ operator
# dot_product = array @ array

print("Dot product of the array with itself:", dot_product)
