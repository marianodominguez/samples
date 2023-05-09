#!/usr/bin/env python3

import pygame,sys
import math

w,h=1440,960

def draw():
  y=0
  x=0
  for i in range(0,w,2):
        y=h/3*math.sin(i/(40*math.pi)) + h/2
        x=i
        pygame.draw.line(screen,white,(w/2,0),(x,y))
        #pygame.draw.line(screen,white,(x,y),(w,h))
        pygame.display.update()

black = pygame.Color('black')
white = pygame.Color('white')

pygame.init()
screen = pygame.display.set_mode((w,h),pygame.RESIZABLE)
screen.fill(black)
draw()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.VIDEORESIZE:
        w,h = event.w,event.h
        draw()
