#!/usr/bin/env python3
import pygame,sys
import math

w,h=800,600

pygame.init()
screen = pygame.display.set_mode((w,h))

iterations = 1000

def orbit(x,y):
    z=complex(0)
    c=complex(x,y)
    i=0
    while i<iterations and abs(z)<4:
        i+=1
        z=z*z+c
    return abs(z)

def color(v):
    return (int(255*v/100) % 255 , int(255*v/100) % 255, 170)

def gradient(v):
    return (int(255*v/100) % 255 , int(255*v/100) % 255, 170)

xmin = -2.5
xmax =  1.0

ymin = -1.5
ymax =  1.5

for xs in range(w):
    pygame.display.update()
    for ys in range(h):
        x=xs*(xmax-xmin)/w+xmin
        y=ys*(ymax-ymin)/h+ymin
        o=orbit(x,y)
        if o>=4:
            screen.set_at((xs,ys),color(o))

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
