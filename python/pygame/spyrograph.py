#!/usr/bin/env python3

import pygame,sys
import math

w,h=800,600

pygame.init()
screen = pygame.display.set_mode((800,600))

red = pygame.Color('red')
yellow = pygame.Color('yellow')
cyan = pygame.Color('cyan')
black = pygame.Color('black')

x=0
y=0
n=10000
px,py=-1,-1

def fn(R,t,k,l):
     x = R*((1-k)*math.cos(t) + l*k*math.cos((1-k)*t/k))
     y = R*((1-k)*math.sin(t) - l*k*math.sin((1-k)*t/k))
     return (x,y)

def plot(x,y,c):
    global px,py
    point = (int(x+w/2), int(h/2-y) )
    if (px>=0 and py>=0):
        pygame.draw.aaline(screen,c,(px,py),point)
    px,py=point

def spyro(R,r,l, color):
    global px,py
    t=0
    k=r/R

    for i in range(0,n):
        t+=math.radians(1)
        #x=r*math.sin(t)
        #y=r*math.cos(t)
        (x,y) = fn(R,t,k,l)
        plot(x,y,color)
    px,py=-1,-1


pygame.display.set_caption('Spyrographs !')

args = [ 
      (300.0, 53.0, 0.9, red),
      (156.0, 56.0, 0.4, yellow),
      (200.0, 48.0, 0.9, cyan),
      (300.0, 45.0, 0.5, pygame.Color('cadetblue')),
      (100.0, 15.0, 0.9, pygame.Color('gray')),
      (250.0, 11.0, 0.9, pygame.Color('magenta'))
      ]
i=0

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN:
        screen.fill(black)
        spyro(*args[i])
        i+=1
        if i>=len(args):
          sys.exit() 
  pygame.display.update()
