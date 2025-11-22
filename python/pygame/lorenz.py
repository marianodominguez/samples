#!/usr/bin/env python3
"""
Lorenz Attractor Visualization

This script visualizes the Lorenz attractor using Pygame.
The Lorenz system is a system of ordinary differential equations first studied by
Edward Lorenz. It is notable for having chaotic solutions for certain parameter values
and initial conditions.

The system is defined by:
dx/dt = sigma * (y - x)
dy/dt = x * (rho - z) - y
dz/dt = x * y - beta * z

This script uses the Runge-Kutta 4th order method (RK4) for numerical integration.
"""

import pygame,sys
import math

# Window dimensions
w,h=1440,960

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('blue'))

# Lorenz system parameters
# r: sigma (Prandtl number)
# s: rho (Rayleigh number)
# b: beta
# d: delta t (time step)
r,s,b,d=10,28,8/3,0.002

# Initial conditions for two trajectories
# x, y, z lists store the current state for each trajectory
x,y,z=[1.2, 1.21] ,[0,0] ,[0,0]
scale=5

def rk4_step(x, y, z, dt, r, s, b):
    """
    Performs a single step of Runge-Kutta 4th order integration.

    Args:
        x, y, z: Current state variables.
        dt: Time step.
        r, s, b: Lorenz system parameters (sigma, rho, beta).

    Returns:
        Updated x, y, z values.
    """
    k1x, k1y, k1z = lorenz(x, y, z, r, s, b)
    k2x, k2y, k2z = lorenz(x + 0.5*dt*k1x, y + 0.5*dt*k1y, z + 0.5*dt*k1z, r, s, b)
    k3x, k3y, k3z = lorenz(x + 0.5*dt*k2x, y + 0.5*dt*k2y, z + 0.5*dt*k2z, r, s, b)
    k4x, k4y, k4z = lorenz(x + dt*k3x, y + dt*k3y, z + dt*k3z, r, s, b)
    x += (dt/6.0)*(k1x + 2*k2x + 2*k3x + k4x)
    y += (dt/6.0)*(k1y + 2*k2y + 2*k3y + k4y)
    z += (dt/6.0)*(k1z + 2*k2z + 2*k3z + k4z)
    return x, y, z

def lorenz(x, y, z, r, s, b):
    """
    Calculates the derivatives of the Lorenz system.

    Args:
        x, y, z: Current state variables.
        r, s, b: Lorenz system parameters.

    Returns:
        dx, dy, dz: Derivatives with respect to time.
    """
    dx = r * (y - x)
    dy = x * (s - z) - y
    dz = x * y - b * z
    return dx, dy, dz

# Main simulation loop
# We run for a large number of steps to visualize the attractor
for i in range(320000):
    # Update and draw both trajectories
    for j in range(2):
        x[j], y[j], z[j] = rk4_step(x[j], y[j], z[j], d, r, s, b)

        # Project 3D coordinates to 2D screen coordinates
        # Simple projection: ignore z for x-position, use z for perspective or just plot x-y?
        # The original code plots x vs y (or similar projection)
        xp = int(w/2 + scale*5.4*x[j])
        yp = int(h/2 - scale*3*y[j])

        if 0 <= xp < w and 0 <= yp < h:
            color = pygame.Color('white') if j == 0 else pygame.Color('red')
            screen.set_at((xp, yp), color)
            screen.set_at((xp+1, yp), color)
            screen.set_at((xp, yp+1), color)
            screen.set_at((xp+1, yp+1), color)
        
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Update display
        pygame.display.update()