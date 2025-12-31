''' Nebula simulation

Press ESC to quit
'''
from numba import cuda
import numpy as np
import pygame,sys
import math
import colorsys
import random

# Window dimensions
w,h=1440,960
r=1

# Number of particles to simulate
NUMBER_OF_ANGLES = 360
PARTICLES_PER_ANGLE = 28  # ~10,000 total particles
NUMBER_OF_PARTICLES = NUMBER_OF_ANGLES * PARTICLES_PER_ANGLE

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('black'))
time=0
x = np.zeros(NUMBER_OF_PARTICLES, dtype=np.int32)
y = np.zeros(NUMBER_OF_PARTICLES, dtype=np.int32)

# Create arrays for angles and radii
angles = np.zeros(NUMBER_OF_PARTICLES, dtype=np.float32)
radii = np.zeros(NUMBER_OF_PARTICLES, dtype=np.float32)

# Distribute particles: each angle gets multiple particles with different radii
for i in range(NUMBER_OF_ANGLES):
    angle = (i / NUMBER_OF_ANGLES) * 2 * np.pi 
    for j in range(PARTICLES_PER_ANGLE):
        idx = i * PARTICLES_PER_ANGLE + j
        angles[idx] = angle
        # Stagger the radii so particles are spread out along each ray
        radii[idx] = (j + random.randint(-10, 10)) * (h // 2) / PARTICLES_PER_ANGLE

d_x = cuda.to_device(x)
d_y = cuda.to_device(y)
d_angles = cuda.to_device(angles)
d_radii = cuda.to_device(radii)

threadsperblock = 256
blockspergrid = (NUMBER_OF_PARTICLES + (threadsperblock - 1)) // threadsperblock
    
@cuda.jit
def step_kernel(x, y, angles, radii, time, w, h, max_radius):
    i = cuda.grid(1)
    if i < x.size:
        # Wrap radius when it exceeds max_radius
        effective_radius = (radii[i] + time ) % max_radius
        effective_radius = max(effective_radius, 100)

        r = effective_radius
        x[i] = int(r * math.cos(angles[i]+time)) + w // 2
        y[i] = int(r * math.sin(angles[i]+time)) + h // 2


max_radius = h // 2
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update time
    time += 1
    screen.fill(pygame.Color('black'))
    # Update particles
    # Run GPU kernel
    step_kernel[blockspergrid, threadsperblock](
        d_x, d_y, d_angles, d_radii, time, w, h, max_radius
    )
    d_x.copy_to_host(x)
    d_y.copy_to_host(y)

    
    # Draw particles
    pixels = pygame.surfarray.pixels3d(screen)
    
    mask = (x >= 0) & (x < w) & (y >= 0) & (y < h)
        # Color based on distance from center (creates gradient effect)
    distances = np.sqrt((x[mask] - w//2)**2 + (y[mask] - h//2)**2)
    colors = np.zeros((mask.sum(), 3), dtype=np.uint8)
    
    # Create color gradient from center to edge
    normalized_dist = np.clip(distances / max_radius, 0, 1)
    colors[:, 0] = (np.sin(normalized_dist * np.pi  * 0.01) * 127 + 128).astype(np.uint8)  # Red
    colors[:, 1] = (np.cos(normalized_dist * np.pi * 0.01) * 127 + 128).astype(np.uint8)  # Green
    colors[:, 2] = 255 - (normalized_dist * 255).astype(np.uint8)  # Blue
    
    # Apply colors to pixels
    pixels[x[mask], y[mask]] = colors
    del pixels
    
    # Update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
    
        