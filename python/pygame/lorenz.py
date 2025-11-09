#!/usr/bin/env python3

import pygame,sys
import math

w,h=1440,960

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('blue'))

r,s,b,d=10,28,8/3,0.002

x,y,z=[1.2, 1.21] ,[0,0] ,[0,0]
scale=5

def rk4_step(x, y, z, dt, r, s, b):
    k1x, k1y, k1z = lorenz(x, y, z, r, s, b)
    k2x, k2y, k2z = lorenz(x + 0.5*dt*k1x, y + 0.5*dt*k1y, z + 0.5*dt*k1z, r, s, b)
    k3x, k3y, k3z = lorenz(x + 0.5*dt*k2x, y + 0.5*dt*k2y, z + 0.5*dt*k2z, r, s, b)
    k4x, k4y, k4z = lorenz(x + dt*k3x, y + dt*k3y, z + dt*k3z, r, s, b)
    x += (dt/6.0)*(k1x + 2*k2x + 2*k3x + k4x)
    y += (dt/6.0)*(k1y + 2*k2y + 2*k3y + k4y)
    z += (dt/6.0)*(k1z + 2*k2z + 2*k3z + k4z)
    return x, y, z

def lorenz(x, y, z, r, s, b):
    dx = r * (y - x)
    dy = x * (s - z) - y
    dz = x * y - b * z
    return dx, dy, dz

for i in range(320000):
    for j in range(2):
        x[j], y[j], z[j] = rk4_step(x[j], y[j], z[j], d, r, s, b)

        xp = int(w/2 + scale*5.4*x[j])
        yp = int(h/2 - scale*3*y[j])

        if 0 <= xp < w and 0 <= yp < h:
            color = pygame.Color('white') if j == 0 else pygame.Color('red')
            pygame.draw.circle(screen, color, (xp, yp), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()