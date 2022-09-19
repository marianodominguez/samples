#!/bin/python 

from email.quoprimime import header_check
import os, sys
import pygame
import math
import random
from pygame.locals import *


if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

sqrt_2 = math.sqrt(2)


def cone():
  for th in range(0,360, 2):
    x1=height/3 * math.sin(math.radians(th))
    y1=height/3 * math.cos(math.radians(th))
    pygame.draw.aaline(screen, pygame.Color('mistyrose1') , adjxy(-height/2 , height/2-10), adjxy(x1,y1) )

def triangle():
  for x in range(int(-width/2),int(width/2),5):
    pygame.draw.aaline(screen, pygame.Color('coral') , adjxy(0,0), adjxy(x,height/2) )
    
def diamond():
    r = height/2
    for i in range(0, 360, 15):
        x=r * math.sin(math.radians(i))
        y=r * math.cos(math.radians(i))
        for j in range (0, 360, 15):
            x1=r * math.sin(math.radians(j))
            y1=r * math.cos(math.radians(j))
            pygame.draw.aaline(screen, pygame.Color('plum') , adjxy(x,y), adjxy(x1,y1) )
    
def curve():
    r = 4/10*height
    for th in range(0,360):
        x = r * math.sin(math.radians(th))
        y = r * math.cos(math.radians(th))
        x1= r * math.cos(math.radians(th)*2)
        y1= r * math.cos(math.radians(th)*2)
        pygame.draw.aaline(screen, pygame.Color('yellow2') , adjxy(x ,y), adjxy(x1,y1) )

def curve2():
    r = height/4
    for th in range(0,360):
        x = r * math.sin(math.radians(th))
        y = r * math.cos(math.radians(th))
        x1= (r+height/5) * math.cos(math.radians(th))
        y1= (r+height/5) * math.cos(math.radians(th))
        pygame.draw.aaline(screen, pygame.Color('yellow') , adjxy(x,y), adjxy(x1,y1) )
        #screen.set_at(adjxy(x,y), (0,255,255))
        #screen.set_at(adjxy(x1,y1), (255,255,0))        
        

def sierpinski_chaos():
    vertex = [(0, height/2), (-width/2, -height/2), (width/2, -height/2)]
    point = (0, height/2)
    for i in range(100000):
        randomVertex = vertex[random.randint(0,2)]
        midpoint = (( randomVertex[0] + point[0] )/2, ( randomVertex[1] + point[1] )/2)
        screen.set_at(adjpt(midpoint), pygame.Color('papayawhip'))
        point = midpoint

def sierpinski(level,vx,vy,l):
    if level==0:
        if (l<=1):
            screen.set_at((vx,vy), pygame.Color('cyan3'))            
        p1 = (vx, vy)
        p2 = (vx - l/2, vy + l/2)
        p3 = (vx + l/2, vy + l/2)
        pygame.draw.polygon(screen, pygame.Color('cyan3'), [p1, p2, p3])
    else:
        sierpinski(level-1 , vx,vy , l/2)
        sierpinski(level-1 , vx - l/4 ,vy + l/4 , l/2)
        sierpinski(level-1 , vx + l/4 ,vy + l/4 , l/2)        

def FD(l):
    global xpos,ypos,alpha
    newx, newy = xpos + l*math.sin(alpha), ypos + l*math.cos(alpha)
    pygame.draw.aaline(screen, pygame.Color('palegreen'), (xpos , ypos),(newx, newy))
    xpos,ypos = newx,newy

def dragon(level, l, i=1):
    global alpha
    if level==0:
        FD(l)
        alpha += math.radians(90 * i)
        FD(l)
    else:
        alpha -= math.radians(45)
        dragon(level - 1, side(l), 1)
        alpha += math.radians(90 * i)        
        dragon(level - 1, side(l), -1)
        alpha += math.radians(45)
             
def adjxy(x,y):
    return (int(x + width/2), int(height/2 -y))

def adjpt(point):
    return adjxy(int(point[0]), int(point[1]))

def side(x):
    return x/2 * sqrt_2 

mode = width,height = 1440,960

pygame.init()

screen = pygame.display.set_mode(mode)

basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Press number keys 1-8', True, pygame.Color('red'), pygame.Color('black'))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
screen.fill((0,0,0))
screen.blit(text, textrect)
pygame.display.update()

l = 0    
ld =0

while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
        sys.exit()
    elif event.type == KEYDOWN:
      screen.fill(pygame.Color('black'))
      if event.key == pygame.K_1:
          cone()
      if event.key == pygame.K_2:
          triangle()
      if event.key == pygame.K_3:
          diamond()
      if event.key == pygame.K_4:
          curve()
      if event.key == pygame.K_5:
          sierpinski(l, width /2, 0 , width)
          if l<9: l = l+1
          else : l=0
      if event.key == pygame.K_6:
          alpha=0
          xpos, ypos = width/3,height/4          
          dragon(ld, height/2)
          if ld<16: ld +=1
          else : ld=0
      if event.key == pygame.K_7:
          curve2()
      if event.key == pygame.K_8:
          sierpinski_chaos()
  pygame.display.update()
  
