import pygame
import sys
import numpy as np

WIDTH, HEIGHT = 1440, 960

# Total possible colors: 256^3 = 16,777,216 (we'll use 16,581,375 = 255^3)
MAX_COLORS = 255 * 255 * 255  # 16,581,375 colors

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# Use 24-bit RGB surface to support full color range
rgb_surf = pygame.Surface((WIDTH, HEIGHT))
rgb_surf.fill(pygame.Color('black'))
clock = pygame.time.Clock()

scale = 0.001

def drawField():
    """Draw the field using vectorized NumPy operations for parallel computation"""
    # Create coordinate grids for all pixels at once
    x = np.arange(WIDTH)
    y = np.arange(HEIGHT)
    X, Y = np.meshgrid(x, y)
    
    # Compute field values for all pixels in parallel
    xs = (X - WIDTH/2) / 10 * scale
    ys = (Y - HEIGHT/2) / 10 * scale
    z = np.abs((xs*xs + ys*ys).astype(np.int64))
    
    # Map to color indices
    color_indices = z % MAX_COLORS
    
    # Decompose into RGB components (vectorized)
    r = color_indices % 255
    g = (color_indices // 255) % 255
    b = (color_indices // (255 * 255)) % 255
    
    # Create RGB array (height, width, 3)
    rgb_array = np.stack([r, g, b], axis=-1).astype(np.uint8)
    
    # Convert to pygame surface using surfarray
    pygame.surfarray.blit_array(rgb_surf, rgb_array.transpose(1, 0, 2))

drawField()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WIDTH,HEIGHT = event.w,event.h
            screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
            rgb_surf = pygame.Surface((WIDTH, HEIGHT))
            rgb_surf.fill(pygame.Color('black'))
            drawField()
    screen.blit(rgb_surf, (0, 0))
    pygame.display.update()
    scale+=0.1
    drawField()
