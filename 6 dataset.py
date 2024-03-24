# Write a Python program that uses NumPy to find the mean, median, and standard deviation of a dataset

import numpy as np

# Sample dataset
dataset = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculate mean
mean_value = np.mean(dataset)

# Calculate median
median_value = np.median(dataset)

# Calculate standard deviation
std_deviation = np.std(dataset)

print("Dataset:", dataset)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
