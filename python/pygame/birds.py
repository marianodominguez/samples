'''
Draw a bird using parametric equations
'''

import pygame,sys
import math

w,h=1440,960
scale=5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((w,h))
screen.fill(pygame.Color('white'))

# Draw the bird
for k in range(-20000, 20000,3):
    a=3*k/45000 + math.sin(17*math.pi/20*math.pow(k/20000,5)) * math.pow(math.cos(41*math.pi*k/20000),6) + (1/3*math.pow(math.cos(41*math.pi*k/20000) ,16) + 1/3*math.pow(math.cos(41*math.pi*k/20000),80) )*math.pow(math.cos(math.pi*k/40000),12)*math.sin(6*math.pi*k/20000)

    b=15/30* math.pow(k/20000,4) - math.cos(17*math.pi/20*math.pow(k/20000,5)) * ( 11/10+45/20*math.pow(math.cos(math.pi*k/40000),8)*math.pow(math.cos(3*math.pi*k/40000),6) ) * math.pow(math.cos(41*math.pi*k/20000),6) + 12/20*math.pow(math.cos(3*math.pi*k/200000),10) * math.pow(math.cos(9*math.pi*k/200000),10) * math.pow(math.cos(18*math.pi*k/200000),10)
    
    r=1/50+1/40*math.pow(math.sin(41*math.pi*k/20000),2)*math.pow(math.sin(9*math.pi*k/200000),2)+1/17*math.pow(math.cos(41*math.pi*k/20000),2)*math.pow(math.cos(math.pi*k/40000),10)

    xp=int(w/2+170*a+100)
    yp=int(h/2-180*b-100)

    if xp>0 and xp<w and yp>0 and yp<h:
        pygame.draw.circle(screen,pygame.Color('black'),(xp,yp),int(abs(r*300)), width=1)
        pygame.display.update()

# Main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()