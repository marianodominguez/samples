#!/usr/bin/env python3

import pygame
import math,sys

w,h=1440,960

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('blue'))

th,ph=0,0
s=math.pi/40
r=300
p1=math.cos(math.pi/6)
p2=math.cos(math.pi/2-p1)
x1,y1=-1,-1
while th<2*math.pi:
    ph=0
    x1=-1
    while ph<2*math.pi:
        th1=th-ph*0.5
        x=r*math.sin(th1)*math.cos(ph)
        y=r*math.sin(th1)*math.sin(ph)
        z=r*math.cos(th1)

        xp=int(-p1*x+p1*y + w/2)
        yp=int((-p2*x-p2*y+z + h/2)*0.85)
        if x1<0:
            screen.set_at((xp,yp),pygame.Color('white'))
        else:
             pygame.draw.aaline(screen, pygame.Color('plum') , (x1,y1), (xp,yp) )
        x1=xp
        y1=yp
        pygame.display.update()
        ph=ph+s
    th=th+s
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()