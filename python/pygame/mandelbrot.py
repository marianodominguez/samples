#!/usr/bin/env python3
import numpy as np
import pygame
import sys

w, h = 1440, 960

pygame.init()
screen = pygame.display.set_mode((w, h))

iterations = 700

def color_heatmap(v, max_iterations):
    if v == max_iterations - 1:  # Point is in the set
        return (0, 0, 0)  # Black
    # Create a smooth color gradient for escaped points
    t = v / max_iterations
    r = int(9 * (1 - t) * t**3 * 255)
    g = int(15 * (1 - t)**2 * t**2 * 255)
    b = int(8.5 * (1 - t)**3 * t * 255)
    return (r, g, b)


def mandelbrot_vectorized(w, h, iterations=500):
    x = np.linspace(-2.0, 1.0, w)
    y = np.linspace(-1.3, 1.3, h)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y
    Z = np.zeros_like(C)

    escape_count = np.zeros(C.shape, dtype=int)

    for i in range(iterations):
        mask = np.abs(Z) <= 4
        Z[mask] = Z[mask]**2 + C[mask]
        escape_count[mask] = i

    return escape_count


# Generate the Mandelbrot set using vectorized method
escape_values = mandelbrot_vectorized(w, h, iterations)

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
