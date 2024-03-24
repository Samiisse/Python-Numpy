#Implement a program that generates a NumPy array with numbers from 0 to 9 and reshapes it into a 3x3 matrix

import numpy as np

# Generate a NumPy array with numbers from 0 to 8
num_array = np.arange(9)

# Reshape the array into a 3x3 matrix
reshaped_array = num_array.reshape(3, 3)

print("Original Array:")
print(num_array)

print("\nReshaped Matrix:")
print(reshaped_array)
