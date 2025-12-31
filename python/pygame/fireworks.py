import pygame,sys
import math
import random
import pygame.time
WIDTH,HEIGHT=1440,960

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
screen.fill(pygame.Color('black'))
colors=[pygame.Color('red'),pygame.Color('green'),pygame.Color('blue'),pygame.Color('yellow'),pygame.Color('magenta'),pygame.Color('cyan')]
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

def animate_line(screen, color, start, end):
    xmin=min(start[0],end[0])
    xmax=max(start[0],end[0])
    ymin=min(start[1],end[1])
    ymax=max(start[1],end[1])

    if abs(xmin-xmax)<=1:
        for y in range(ymin,ymax):
            screen.set_at((xmin,y), color)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        return

    for x in range(xmin,xmax):
        y=int(start[1]+(end[1]-start[1])*(x-start[0])/(end[0]-start[0]))
        screen.set_at((x,y), color)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def draw_firework(xc,yc, radius):
    color=random.choice(colors)
    for angle in range(0,360,10+random.randint(0,10)):
        x=int(xc+math.cos(math.radians(angle))*radius)
        y=int(yc+math.sin(math.radians(angle))*radius)
        animate_line(screen, color, (xc,yc), (x,y))

def draw_fireworks():
    for i in range(10):
        draw_firework(random.randint(0,WIDTH),random.randint(0,HEIGHT),random.randint(100,200))

def main():
    global WIDTH,HEIGHT
    draw_fireworks()
    text = font.render('HAPPY 2026!', True, (255, 255, 255))
    screen.blit(text, (WIDTH//2-100, HEIGHT//2-100))
    pygame.display.update()

    #wait for key press
    pygame.event.wait()
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WIDTH,HEIGHT = event.w,event.h
                screen.fill(pygame.Color('black'))
        screen.fill(pygame.Color('black'))
if __name__ == '__main__':
    main()