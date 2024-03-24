#Write a function that takes a NumPy array and returns a new array with all elements squared

import numpy as np

def square_array_elements(input_array):
    # Square all elements of the input array
    squared_array = np.square(input_array)
    return squared_array

# Example usage:
input_array = np.array([1, 2, 3, 4, 5])
result_array = square_array_elements(input_array)
print("Input Array:", input_array)
print("Array with Squared Elements:", result_array)
