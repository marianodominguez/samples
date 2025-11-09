#!/usr/bin/env python3
import numpy as np
import pygame
import sys
from numba import jit, prange
import math

w, h = 1440, 960
iterations = 700
zoom_factor = 0.5  # how much to zoom in each click

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Mandelbrot Zoom (click to zoom)")

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
def compute_mandelbrot(width, height, max_iter, min_x, max_x, min_y, max_y):
    """Compute Mandelbrot set using CPU parallelization"""
    output = np.zeros((height, width), dtype=np.int32)
    
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


def draw_mandelbrot(min_x, max_x, min_y, max_y):
    escape_values = compute_mandelbrot(w, h, iterations, min_x, max_x, min_y, max_y)
    for y in range(h):
        for x in range(w):
            v = escape_values[y, x]
            screen.set_at((x, y), color_heatmap(v, iterations))
    pygame.display.update()

# initial view range
min_x, max_x = -2.0, 1.0
min_y, max_y = -1.3, 1.3


while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left click to zoom in
            mouse_x, mouse_y = event.pos
            # Map pixel to complex plane
            click_real = min_x + (max_x - min_x) * mouse_x / w
            click_imag = min_y + (max_y - min_y) * mouse_y / h

            # Zoom around click
            range_x = (max_x - min_x) * zoom_factor
            range_y = (max_y - min_y) * zoom_factor
            min_x = click_real - range_x / 2
            max_x = click_real + range_x / 2
            min_y = click_imag - range_y / 2
            max_y = click_imag + range_y / 2

            draw_mandelbrot(min_x, max_x, min_y, max_y)

        elif event.button == 3:  # Right click to zoom out
            mouse_x, mouse_y = event.pos
            click_real = min_x + (max_x - min_x) * mouse_x / w
            click_imag = min_y + (max_y - min_y) * mouse_y / h

            range_x = (max_x - min_x) / zoom_factor
            range_y = (max_y - min_y) / zoom_factor
            min_x = click_real - range_x / 2
            max_x = click_real + range_x / 2
            min_y = click_imag - range_y / 2
            max_y = click_imag + range_y / 2

            draw_mandelbrot(min_x, max_x, min_y, max_y)