'''Moire pattern with antialiasing

see https://en.wikipedia.org/wiki/Moire_pattern

Press ESC to quit
'''

import pygame,sys

w,h=1440,960

# Colors
black = pygame.Color('black')
white = pygame.Color('white')

# Draw Moire pattern
def draw_moire():
  y=0
  for x in range(0,w,2):
    pygame.draw.aaline(screen,black,(w/2,h/2),(x,0))
    pygame.draw.aaline(screen,white,(w/2,h/2),(x+1,0))
    pygame.draw.aaline(screen,black,(w/2,h/2),(x,h))
    pygame.draw.aaline(screen,white,(w/2,h/2),(x+1,h))
    if y<h:
        pygame.draw.aaline(screen,black,(w/2,h/2),(0,y))
        pygame.draw.aaline(screen,white,(w/2,h/2),(0,y+1))
        pygame.draw.aaline(screen,black,(w/2,h/2),(w,y))
        pygame.draw.aaline(screen,white,(w/2,h/2),(w,y+1))
    y+=2
    pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((w,h),pygame.RESIZABLE )
screen.fill(black)
draw_moire()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.VIDEORESIZE:
        w,h = event.w,event.h
        screen.fill(black)
        draw_moire()
