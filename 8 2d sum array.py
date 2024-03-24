#Given a list of lists, create a 2D NumPy array and find the sum of elements in each row and column

import numpy as np

def sum_of_rows_and_columns(list_of_lists):
    # Convert the list of lists to a 2D NumPy array
    array_2d = np.array(list_of_lists)
    
    # Calculate the sum of elements in each row
    row_sums = np.sum(array_2d, axis=1)
    
    # Calculate the sum of elements in each column
    column_sums = np.sum(array_2d, axis=0)
    
    return row_sums, column_sums

# Example usage:
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sums, column_sums = sum_of_rows_and_columns(list_of_lists)

print("2D NumPy Array:")
print(np.array(list_of_lists))
print("\nSum of Elements in Each Row:", row_sums)
print("Sum of Elements in Each Column:", column_sums)
