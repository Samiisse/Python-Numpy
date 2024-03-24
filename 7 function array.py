# Create a function that takes a list of numbers and returns the NumPy array sorted in ascending order

import numpy as np

def sort_array(numbers):
    # Convert the list to a NumPy array
    num_array = np.array(numbers)
    
    # Sort the array in ascending order
    sorted_array = np.sort(num_array)
    
    return sorted_array

# Example usage:
numbers_list = [5, 2, 8, 1, 9, 3]
sorted_result = sort_array(numbers_list)
print("Sorted Array:", sorted_result)
