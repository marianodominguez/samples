#!/usr/bin/env python3

import pygame
import math,sys

w,h=1440,960

pygame.init()
screen = pygame.display.set_mode((w,h), pygame.RESIZABLE)
screen.fill(pygame.Color('blue'))

s=math.pi/40
r=300
p1=math.cos(math.pi/7)
p2=math.cos(math.pi/7-p1)

def draw():
    global w,h
    x1,y1=-1,-1
    th=0
    while th<=2*math.pi:
        ph=0
        x1=-99
        while ph<=2*math.pi:
            th1=th-ph*0.5

            x=(10*math.cos(th)+50)*math.cos(ph)
            y=(10*math.cos(th)+50)*math.sin(ph)
            z=10*math.sin(th)

            xp=-p1*x+p1*y 
            yp=-p2*x-p2*y+z
            xp=int( xp*w/200 +w/2 )
            yp=int( yp*h/200 + h/2 )
            if x1==-99:
                screen.set_at((xp,yp),pygame.Color('white'))
            else:
                pygame.draw.aaline(screen, pygame.Color('plum') , (x1,y1), (xp,yp) )
            x1=xp
            y1=yp
            ph=ph+s
        pygame.display.update()
        th=th+s
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                w,h = event.w,event.h
                th=0
                ph=0
                screen.fill(pygame.Color('blue'))

draw()
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.VIDEORESIZE:
        w,h = event.w,event.h
        screen.fill(pygame.Color('blue'))
        draw()