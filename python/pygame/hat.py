'''Hat Function Curve

see https://en.wikipedia.org/wiki/Hat_function

Press ESC to quit
'''

import pygame,sys
import math

RESIZE=False

def plot(xx,yy,zz,p,q):
   x1=xx+zz+p
   y1=-yy+zz+q
   screen.set_at((int(x1),int(y1)),pygame.Color('white'))
   if y1==0: return
   screen.set_at((int(x1),int(y1-1)),pygame.Color('white'))

def draw():
  y=0
  p=int(w/2)
  q=int(h/2)
  xp=144*p/160
  xr=1.5*math.pi
  yp=56*q/100
  yr=1
  zp=64*q/200
  xf=xr/xp
  yf=yp/yr
  zf=xr/zp
  for z in range(-q,q-1):
    if z<-zp or z>zp: continue
    zt=z*xp/zp
    zz=z
    xl=int(0.5+math.sqrt(xp*xp-zt*zt))
    for x in range(-xl,xl):
       xt=math.sqrt(x*x+zt*zt)*xf
       xx=x
       yy=(math.sin(xt)+0.4*math.sin(3*xt))*yf
       plot(xx,yy,zz,p,q)
    pygame.display.flip()
    #pygame.event.get()

w,h=1440,960

black = pygame.Color('black')
white = pygame.Color('white')

pygame.init()
screen = pygame.display.set_mode((w,h), pygame.RESIZABLE | pygame.DOUBLEBUF)
screen.fill(black)
draw()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.VIDEORESIZE:
        w,h = event.w,event.h
        RESIZE=True
    if RESIZE:
      screen.fill(black)
      draw()
      RESIZE=False
