#Given a list of numbers, create a NumPy array and find the sum and product of its elements

import numpy as np

# List of numbers
numbers_list = [2, 3, 5, 7, 11, 13]

# Create a NumPy array
num_array = np.array(numbers_list)

# Find the sum of elements
sum_of_elements = np.sum(num_array)

# Find the product of elements
product_of_elements = np.prod(num_array)

print("NumPy Array:", num_array)
print("Sum of elements:", sum_of_elements)
print("Product of elements:", product_of_elements)
