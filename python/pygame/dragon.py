#!/usr/bin/env python3
import pygame,sys

w,h=800,600

black = pygame.Color('black')
white = pygame.Color('white')

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(black)

def dragon(level,l,x,y):
  if level==1:
    pygame.draw.line(screen,white,(x,y),(x+l,y))
    pygame.draw.line(screen,white,(x,y),(x,y+l))
  else:
    dragon(level-1,l/3,x,y)
    

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
