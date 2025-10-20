#!/usr/bin/env python3
import numpy as np
import pygame
import sys
from numba import jit, prange
import math

w, h = 1440, 960
iterations = 700

pygame.init()
screen = pygame.display.set_mode((w, h))

def color_heatmap(v, max_iterations):
    if v == max_iterations - 1:  # Point is in the set
        return (0, 0, 0)  # Black
    # Create a smooth color gradient for escaped points
    t = v / max_iterations
    r = int(9 * (1 - t) * t**3 * 255)
    g = int(15 * (1 - t)**2 * t**2 * 255)
    b = int(8.5 * (1 - t)**3 * t * 255)
    return (r, g, b)


@jit(nopython=True, parallel=True)
def compute_mandelbrot(width, height, max_iter):
    """Compute Mandelbrot set using CPU parallelization"""
    output = np.zeros((height, width), dtype=np.int32)
    
    # Define the complex plane range
    min_x, max_x = -2.0, 1.0
    min_y, max_y = -1.3, 1.3
    
    # Compute each row in parallel
    for y in prange(height):
        for x in range(width):
            # Map pixel coordinates to complex plane
            real = min_x + (max_x - min_x) * x / width
            imag = min_y + (max_y - min_y) * y / height
            
            # Initialize values for iteration
            c_real = real
            c_imag = imag
            z_real = 0.0
            z_imag = 0.0
            
            # Iterate until escape or max iterations
            for i in range(max_iter):
                # Calculate z = z^2 + c
                new_real = z_real * z_real - z_imag * z_imag + c_real
                new_imag = 2 * z_real * z_imag + c_imag
                
                z_real = new_real
                z_imag = new_imag
                
                # Check if point has escaped
                if (z_real * z_real + z_imag * z_imag) > 4.0:
                    output[y, x] = i
                    break
            else:
                output[y, x] = max_iter - 1
                
    return output


# Generate the Mandelbrot set using CPU parallelization
escape_values = compute_mandelbrot(w, h, iterations)

# Draw the Mandelbrot set
for y in range(h):
    for x in range(w):
        v = escape_values[y, x]
        screen.set_at((x, y), color_heatmap(v, iterations))

pygame.display.update()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
