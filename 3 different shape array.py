#Create a NumPy array and reshape it into a different shape.

import numpy as np

# Create a NumPy array
original_array = np.arange(12)  # Creates an array with elements from 0 to 11

print("Original Array:")
print(original_array)

# Reshape the array into a different shape
reshaped_array = original_array.reshape(3, 4)  # Reshape into a 3x4 array

print("\nReshaped Array:")
print(reshaped_array)
