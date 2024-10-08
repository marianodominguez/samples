#!/usr/bin/env python3

import pygame,sys
import math
w,h=1440,960

def adjxy(x,y):
    return (int(x + w/2), int(h/2 -y))

pygame.init()
screen = pygame.display.set_mode((w,h), pygame.RESIZABLE)
screen.fill(pygame.Color('black'))

LUT_SIZE=70
buf=[-99]*(LUT_SIZE+1)
sbuf=[-99]*(LUT_SIZE+1)

p1=math.cos(math.pi/6)
p2=math.cos(math.pi/2-p1)

def draw_klein():
    v=0
    u=0
    idx=0
    while v<2*math.pi:
        cosv=math.cos(v)
        sinv=math.sin(v)
        pygame.display.update()
        while u<math.pi:
            if idx>LUT_SIZE or buf[idx]==-99 :
                cosu=math.cos(u)
                if idx<LUT_SIZE :buf[idx]=cosu
            else:
                cosu=buf[idx]
            if idx>LUT_SIZE or sbuf[idx]==-99:
                sinu=math.sin(u)
                if idx<LUT_SIZE : sbuf[idx]=sinu
            else:
                sinu=sbuf[idx]

            c7u=cosu**7
            c6u=cosu**6
            c5u=cosu**5
            c4u=cosu**4
            c3u=cosu**3

            x=(-2/15)*cosu*(3*cosv-30*sinu+90*c4u*sinu-60*c6u*sinu+5*cosu*cosv*sinu)
            t1=3*cosv-3*cosu*cosu*cosv-48*c4u*cosv+48*c6u*cosv-60
            y=-1/15*sinu*(t1*sinu+5*cosu*cosv*sinv-5*c3u*cosv*sinu-80*c5u*cosv*sinu+80*c7u*cosv*sinu)
            z=(2/15)*(3+5*cosu*sinu)*sinv
            x=150*x+200
            y=150*y
            z=150*z+500
            xp=int(-p1*x+p1*y)
            yp=int(-p2*x-p2*y+z)
            if u==0:
                screen.set_at(adjxy(xp,yp),pygame.Color('plum'))
                x1=xp
                y1=yp
            else:
                pygame.draw.aaline(screen, pygame.Color('plum') , adjxy(xp,yp), adjxy(x1,y1) )
                x1=xp
                y1=yp
            u=u+math.pi/LUT_SIZE
            idx=idx+1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                w=event.w
                h=event.h
                screen.fill(pygame.Color('black'))
                u=0
                v=0
                idx=0

        v=v+math.pi/LUT_SIZE
        u=0
        idx=0
    
draw_klein()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            w=event.w
            h=event.h
            screen.fill(pygame.Color('black'))
            draw_klein()
