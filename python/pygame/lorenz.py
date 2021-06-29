#!/usr/bin/env python
import pygame,sys
import math

w,h=1440,960

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('blue'))

r,s,b,d=10,28,8/3,0.002

x,y,z=0.1,0,0
scale=5

for i in range(320000):
    xp=int(w/2+scale*5.4*x)
    yp=int(h/2-scale*3*y)
    if xp>0 and xp<w and yp>0 and yp<h:
        screen.set_at((xp,yp),pygame.Color('white'))
        pygame.display.update()
    xx=x+d*r*(y-x)
    yy=y+d*(x*(s-z)-y)
    z=z+d*(x*y-b*z)
    x=xx
    y=yy
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()