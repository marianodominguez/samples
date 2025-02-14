import numpy as np

# Matriz 3x3 con los elementos reales
matrix = [
    [3, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def det(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
    return det

print("El determinante es:", det(matrix))

det2 = np.linalg.det(matrix)
print(f"El determinante2 es: {det2:.3f}")