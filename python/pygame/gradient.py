import pygame
import sys
import numpy as np
from numba import prange,jit

WIDTH, HEIGHT = 1440, 960


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# Use 24-bit RGB surface to support full color range
rgb_surf = pygame.Surface((WIDTH, HEIGHT))
rgb_surf.fill(pygame.Color('blue'))
clock = pygame.time.Clock()

def drawField(width, height):
    # Generate all random values at once (vectorized)
    z = np.random.randint(0, height, size=(width, height))
    
    # Create output array with default blue color
    out = np.zeros((width, height, 3), dtype=np.uint8)
    out[:, :, 2] = 255  # Set blue channel
    
    # Create mask for white pixels (where z < y)
    y_coords = np.arange(height)
    mask = z < y_coords[np.newaxis, :]
    
    # Set white pixels where mask is True
    out[mask] = [255, 255, 255]
    
    return out

rgb_surf.fill(pygame.Color('blue'))
out = drawField(WIDTH, HEIGHT)
pygame.surfarray.blit_array(rgb_surf, out)
screen.blit(rgb_surf, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WIDTH,HEIGHT = event.w,event.h
            screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
            rgb_surf = pygame.Surface((WIDTH, HEIGHT))
            rgb_surf.fill(pygame.Color('blue'))
            out = drawField(WIDTH, HEIGHT)
            pygame.surfarray.blit_array(rgb_surf, out)
    
    screen.blit(rgb_surf, (0, 0))
    pygame.display.flip()
    clock.tick(60)

