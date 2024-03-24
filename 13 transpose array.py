#Implement a function that takes a NumPy array and returns the transpose of the array.

import numpy as np

def transpose_array(input_array):
    """
    Transpose a NumPy array.

    Args:
    input_array (numpy.ndarray): Input NumPy array.

    Returns:
    numpy.ndarray: Transpose of the input array.
    """
    return np.transpose(input_array)

# Example usage:
input_array = np.array([[1, 2, 3],
                        [4, 5, 6]])

transposed_array = transpose_array(input_array)
print("Original Array:")
print(input_array)
print("\nTransposed Array:")
print(transposed_array)
