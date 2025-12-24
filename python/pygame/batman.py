'''
Draw Batman logo

batman function from https://www.desmos.com/calculator/6qjyqjyqjy

'''

import pygame
import math,sys

WIDTH,HEIGTH=1440,960
# flag to resize the window
RESIZE=False

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGTH), pygame.RESIZABLE)
screen.fill(pygame.Color('blue'))

def Hs(a):
    """Heaviside function"""
    if a<0:  return 0
    if a==0: return 1/2
    return 1

def pow2(x):
    """Square function"""
    return x*x

def sgn(x):
    """Sign function"""
    if x<0: return -1
    return 1

def sqrt(x):
    """Square root function"""
    if x>0: return math.sqrt(x)
    return 0

def abs(x):
    """Absolute value function"""
    return math.fabs(x)

def draw():
    """Draw Batman logo"""
    global WIDTH,HEIGTH
    x1,y1=-1,-1
    th=0

    x=-7
    while x<=7:
        w=3*sqrt(1-(x/7)*(x/7))
        l=(6/7)*sqrt(10) + (3+x)/2 -3/7*sqrt(10)*sqrt(4-(x+1)*(x+1))
        h= ( 3*( abs(x-1/2) + abs(x+1/2) + 6 ) - 11 * ( abs(x-3/4) + abs(x+3/4) ) ) / 2
        r=6/7*sqrt(10)+(3-x)/2-3/7*sqrt(10)*sqrt((4-(x-1)*(x-1)))
        yt=(h-l)*Hs(x+1)+(r-h)*Hs(x-1)+(l-w)*Hs(x+3)+(w-r)*Hs(x-3)+w
        a=abs(x/2) + sqrt( 1-pow2( abs(abs(x)-2) -1) ) - (3*sqrt(33)-7)/112 * x*x + 3 * sqrt(1 - (x/7)*(x/7) -3)
        yb=(1/2)*a*(sgn(x+4) - sgn(x-4))- 3*sqrt(1-(x/7)*(x/7))
        yt=HEIGTH/3+70*yt
        yb=HEIGTH/3+70*yb
        xp=(x+7)*WIDTH/(20)+WIDTH/6
        pygame.draw.aaline(screen, pygame.Color('yellow') , (xp,2*HEIGTH/3-yt), (xp,2*HEIGTH/3-yb) )
        x+=0.011

        pygame.display.update()

def main():
    """Main function"""
    global RESIZE
    draw()
    while 1:
        pygame.event.pump()
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WIDTH,HEIGTH = event.w,event.h
            RESIZE=True
        if RESIZE:
            screen.fill(pygame.Color('blue'))
            draw()
            RESIZE=False

if __name__ == '__main__':
    main()