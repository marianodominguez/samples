import pygame,sys

WIDTH,HEIGHT=1440,960

palette = [
    pygame.Color(0,x//2,x) for x in range(0,256,26)
]
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
indexed_surf = pygame.Surface((WIDTH, HEIGHT), 0, 8)
indexed_surf.fill(pygame.Color('black'))
indexed_surf.set_palette(palette)
clock = pygame.time.Clock()

def drawField():
    for x in range(0,WIDTH):
        for y in range(0,HEIGHT):
            xs=(x-WIDTH/2)/7
            ys=(y-HEIGHT/2)/7
            z= (int(xs/2)^int(ys/2)) % len(palette)
            indexed_surf.set_at((x,y),z)

def heatmap(z):
    if z<len(palette):
        return palette[z]
    else:
        return palette[-1]

drawField()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WIDTH,HEIGHT = event.w,event.h
            screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
            indexed_surf = pygame.Surface((WIDTH, HEIGHT), 0, 8)
            indexed_surf.fill(pygame.Color('black'))
            drawField()
            indexed_surf.set_palette(palette)
    screen.blit(indexed_surf, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    #rotate the palette
    palette = palette[1:]+palette[:1]
    indexed_surf.set_palette(palette)
