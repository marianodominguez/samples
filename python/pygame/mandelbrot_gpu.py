#!/usr/bin/env python3
from numba import cuda
import numpy as np
import pygame
import sys

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

# ---------------- GPU KERNEL ----------------
@cuda.jit
def compute_mandelbrot(max_iter, min_x, max_x, min_y, max_y, output):
    
    height, width = output.shape # Get image dimensions
    x, y = cuda.grid(2) # Get pixel coordinates
    
    if x < width and y < height:
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


def draw_mandelbrot(min_x, max_x, min_y, max_y):
    output = np.zeros((h, w), dtype=np.int32) # Prepare output array
    d_output = cuda.to_device(output) # Copy to device
    threadsperblock = (16, 16) # Define block size

    blockspergrid_x = (w + threadsperblock[0] - 1) // threadsperblock[0]
    blockspergrid_y = (h + threadsperblock[1] - 1) // threadsperblock[1]
    blockspergrid = (blockspergrid_x, blockspergrid_y) # Define grid size

    compute_mandelbrot[blockspergrid, threadsperblock](iterations, min_x, max_x, min_y, max_y, d_output)
    escape_values = d_output.copy_to_host()

    # Use a numpy rgb array for faster pixel setting
    rgb = np.zeros((h, w, 3), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            v = escape_values[y, x]
            rgb[y,x] = color_heatmap(v, iterations)
    surf = pygame.surfarray.make_surface(np.transpose(rgb, (1, 0, 2)))
    screen.blit(surf, (0, 0))
    pygame.display.flip()

# initial view range
min_x, max_x = -2.0, 1.0
min_y, max_y = -1.3, 1.3

# New helper to centralize zoom calculation
def zoom_at(center_real, center_imag, scale, min_x, max_x, min_y, max_y):
    range_x = (max_x - min_x) * scale
    range_y = (max_y - min_y) * scale
    new_min_x = center_real - range_x / 2
    new_max_x = center_real + range_x / 2
    new_min_y = center_imag - range_y / 2
    new_max_y = center_imag + range_y / 2
    return new_min_x, new_max_x, new_min_y, new_max_y

draw_mandelbrot(min_x, max_x, min_y, max_y)

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

            min_x, max_x, min_y, max_y = zoom_at(click_real, click_imag, zoom_factor, min_x, max_x, min_y, max_y)
            draw_mandelbrot(min_x, max_x, min_y, max_y)

        elif event.button == 3:  # Right click to zoom out
            mouse_x, mouse_y = event.pos
            click_real = min_x + (max_x - min_x) * mouse_x / w
            click_imag = min_y + (max_y - min_y) * mouse_y / h

            min_x, max_x, min_y, max_y = zoom_at(click_real, click_imag, 1.0 / zoom_factor, min_x, max_x, min_y, max_y)
            draw_mandelbrot(min_x, max_x, min_y, max_y)

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        # Predefined zoom point
        zp_x = -0.990000030001
        zp_y = 0.277500004

        min_x, max_x, min_y, max_y = zoom_at(zp_x, zp_y, zoom_factor, min_x, max_x, min_y, max_y)
        draw_mandelbrot(min_x, max_x, min_y, max_y)