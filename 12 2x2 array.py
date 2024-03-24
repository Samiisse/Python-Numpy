#Create a program that uses NumPy to calculate the inverse of a 2x2 matrix

import numpy as np

def main():
    # Define a 2x2 matrix
    matrix = np.array([[4, 7],
                       [2, 6]])

    # Calculate the inverse of the matrix
    inverse_matrix = np.linalg.inv(matrix)

    print("Original Matrix:")
    print(matrix)

    print("\nInverse Matrix:")
    print(inverse_matrix)

if __name__ == "__main__":
    main()
