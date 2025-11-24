#!/usr/bin/env python3
from numba import cuda
import numpy as np
import pygame,sys
import math
import colorsys

# Window dimensions
w,h=1440,960

# Number of particles to simulate
NUMBER_OF_PARTICLES=60000

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('black'))

# Lorenz system constants
# r (rho): Rayleigh number
# s (sigma): Prandtl number
# b (beta): Geometric factor
# d (dt): Time step
r,s,b,d=10,28,8/3,0.002

# Initialize state as numpy arrays, add a random offset to each particle
# We use float32 for GPU compatibility and performance
x = np.array(1.2 + np.random.random(NUMBER_OF_PARTICLES) * 8.0, dtype=np.float32)
y = np.array(0.0 + np.random.random(NUMBER_OF_PARTICLES) * 8.0, dtype=np.float32)
z = np.array(0.0 + np.random.random(NUMBER_OF_PARTICLES) * 8.0, dtype=np.float32)
scale=5

# CUDA device function to calculate Lorenz derivatives
# @cuda.jit(device=True) compiles this function to run on the GPU
# It can only be called from other device functions or kernels
@cuda.jit(device=True)
def lorenz(x, y, z, r, s, b):
    dx = r * (y - x)
    dy = x * (s - z) - y
    dz = x * y - b * z
    return dx, dy, dz

# CUDA device function for Runge-Kutta 4th order integration
# This provides a more accurate approximation of the next state than Euler method
@cuda.jit(device=True)
def rk4_step(x, y, z, dt, r, s, b):
    k1x, k1y, k1z = lorenz(x, y, z, r, s, b)
    k2x, k2y, k2z = lorenz(x + 0.5*dt*k1x, y + 0.5*dt*k1y, z + 0.5*dt*k1z, r, s, b)
    k3x, k3y, k3z = lorenz(x + 0.5*dt*k2x, y + 0.5*dt*k2y, z + 0.5*dt*k2z, r, s, b)
    k4x, k4y, k4z = lorenz(x + dt*k3x, y + dt*k3y, z + dt*k3z, r, s, b)
    x += (dt/6.0)*(k1x + 2*k2x + 2*k3x + k4x)
    y += (dt/6.0)*(k1y + 2*k2y + 2*k3y + k4y)
    z += (dt/6.0)*(k1z + 2*k2z + 2*k3z + k4z)
    return x, y, z

# CUDA kernel to update all particles in parallel
# This is the entry point for the GPU execution
@cuda.jit
def step_kernel(x, y, z, dt, r, s, b):
    # Get the unique thread ID
    i = cuda.grid(1)
    # Ensure we don't access out of bounds if grid size > array size
    if i < x.size:
        x[i], y[i], z[i] = rk4_step(x[i], y[i], z[i], dt, r, s, b)

# Configure grid
# threadsperblock: Number of threads in each block (standard is 32, 64, 128, etc.)
# blockspergrid: Number of blocks needed to cover all particles
threadsperblock = 32
blockspergrid = (x.size + (threadsperblock - 1)) // threadsperblock

# Copy initial state to device (GPU memory)
d_x = cuda.to_device(x)
d_y = cuda.to_device(y)
d_z = cuda.to_device(z)

# Precompute colors for each particle
# This avoids calculating colors in the render loop
colors = np.zeros((NUMBER_OF_PARTICLES, 3), dtype=np.uint8)
tsp = np.linspace(0, 1, NUMBER_OF_PARTICLES, dtype=np.float32)

for idx, hue_val in enumerate(tsp):
    rc, gc, bc = colorsys.hsv_to_rgb(hue_val, 1.0, 1.0)
    colors[idx] = (int(rc*255), int(gc*255), int(bc*255))

for i in range(320000):
    # Launch kernel to update physics on GPU
    step_kernel[blockspergrid, threadsperblock](d_x, d_y, d_z, d, r, s, b)
    
    # Copy updated state back to host (CPU memory) for rendering
    # In a more advanced setup, we would map OpenGL buffers to avoid this copy
    d_x.copy_to_host(x)
    d_y.copy_to_host(y)
    # z is not used for projection in 2D, but is updated for physics
    
    # Clear screen
    screen.fill(pygame.Color('black'))
    
    # Vectorized projection: Convert all 3D coordinates to 2D screen coordinates at once
    # This is much faster than a Python loop
    xp = (w/2 + scale*5.4*x).astype(np.int32)
    yp = (h/2 - scale*3*y).astype(np.int32)
    
    # Create a mask to filter out particles that are off-screen
    mask = (xp >= 0) & (xp < w) & (yp >= 0) & (yp < h)
    
    # Direct pixel access using surfarray
    # This allows us to set thousands of pixels at once using NumPy indexing
    pixels = pygame.surfarray.pixels3d(screen)
    pixels[xp[mask], yp[mask]] = colors[mask]
    pixels[xp[mask]+1, yp[mask]] = colors[mask]
    pixels[xp[mask], yp[mask]+1] = colors[mask]
    pixels[xp[mask]+1, yp[mask]+1] = colors[mask]
    
    del pixels # Unlock the surface
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()