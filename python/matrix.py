'''
Calculate the determinant of a matrix

Calculate the determinant of a matrix using the Leibniz formula


'''
import numpy as np

# Matrix 3x3 with real elements
matrix = [
    [3, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculate the determinant of a matrix
def det(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
    return det

# Print the determinant
print("The determinant is:", det(matrix))

# Calculate the determinant using numpy
det2 = np.linalg.det(matrix)
print(f"The determinant2 is: {det2:.3f}")