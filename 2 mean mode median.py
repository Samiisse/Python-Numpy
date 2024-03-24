# Generate a NumPy array of random numbers and calculate its mean, median, and standard deviation.

import numpy as np

# Generate a NumPy array of random numbers
np.random.seed(0)  # Set seed for reproducibility
random_array = np.random.rand(100)  # Generate 100 random numbers between 0 and 1

# Calculate mean, median, and standard deviation
mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)

# Print the results
print("Random Array:", random_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

