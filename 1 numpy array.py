#Create a NumPy array from a Python list and perform basic operations like addition, multiplication, etc.

import numpy as np

# Create a Python list
python_list = [1, 2, 3, 4, 5]

# Create a NumPy array from the Python list
numpy_array = np.array(python_list)

# Print the NumPy array
print("NumPy array:", numpy_array)

# Perform basic operations
addition_result = numpy_array + 2
multiplication_result = numpy_array * 3
exponential_result = np.exp(numpy_array)

# Print the results
print("Addition result:", addition_result)
print("Multiplication result:", multiplication_result)
print("Exponential result:", exponential_result)

