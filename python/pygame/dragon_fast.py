#!/usr/bin/env python3
import pygame,sys
import math

w,h=1440,960

pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('black'))
s=[0 for i in range(0,240)]
x=1020
y=380
h=0
v=5
s[0]=14
s[1]=1
p=2

def dragon():
    global p,n,s,a,x,y,h,v,u,w,t
    p=p-2
    n=s[p]
    a=s[p+1]
    if n==0:
        u=x+h
        w=y-v
        pygame.draw.line(screen,pygame.Color('yellow'),(x,y),(u,w))
        pygame.display.update()
        x=u
        y=w
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        return
    s[p]=n-1
    s[p+1]=-1
    s[p+2]=a
    s[p+3]=n-1
    s[p+4]=1
    p=p+5
    dragon()
    p=p-1
    a=s[p]
    t=-a*h
    h=a*v
    v=t
    dragon()
    return
        
dragon()
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()






