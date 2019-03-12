#!/usr/bin/env python
import pygame,sys

w,h=1280,720

black = pygame.Color('black')
white = pygame.Color('white')

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(black)
y=0
for x in range(0,w,2):
        pygame.draw.line(screen,black,(w/2,h/2),(x,0))
        pygame.draw.line(screen,white,(w/2,h/2),(x+1,0))
        pygame.draw.line(screen,black,(w/2,h/2),(x,h))
        pygame.draw.line(screen,white,(w/2,h/2),(x+1,h))
        if y<h:
            pygame.draw.line(screen,black,(w/2,h/2),(0,y))
            pygame.draw.line(screen,white,(w/2,h/2),(0,y+1))
            pygame.draw.line(screen,black,(w/2,h/2),(w,y))
            pygame.draw.line(screen,white,(w/2,h/2),(w,y+1))
        y+=2
        pygame.display.update()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
