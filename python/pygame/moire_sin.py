#!/usr/bin/env python3
import pygame,sys
import math

w,h=800,600

black = pygame.Color('black')
white = pygame.Color('white')

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(black)
y=0
x=0
for i in range(0,w,2):
        y=h/2*math.sin(i/(40*math.pi)) + h/2
        x=i
        pygame.draw.line(screen,white,(0,0),(x,y))
        pygame.draw.line(screen,white,(x,y),(w,h))
        pygame.display.update()
        pygame.event.get()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
