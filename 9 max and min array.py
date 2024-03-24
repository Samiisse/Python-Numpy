#Implement a program that generates a random NumPy array and finds the maximum and minimum values

import numpy as np
def find_max_and_min(array):
    # Find the maximum value
    max_value = np.max(array)
    
    # Find the minimum value
    min_value = np.min(array)
    
    return max_value, min_value

# Generate a random NumPy array
random_array = np.random.randint(0, 100, size=(5, 5))  # Generating a 5x5 array with random integers between 0 and 99

# Find the maximum and minimum values
max_value, min_value = find_max_and_min(random_array)

print("Random NumPy Array:")
print(random_array)
print("\nMaximum Value:", max_value)
print("Minimum Value:", min_value)


#In this program:

#We define a function find_max_and_min() that takes a NumPy array as input.
#Inside this function, we use np.max() and np.min() functions to find the maximum and minimum values in the array, respectively.
#We then generate a random NumPy array using np.random.randint().
#Finally, we call the find_max_and_min() function with the random array as input and print the maximum and minimum values.
#This program will generate a random NumPy array each time it is executed and then find the maximum and minimum values within that array.





