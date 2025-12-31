import pygame,sys
import numpy as np
import math
import random
import pygame.time
from numba import jit,prange
import gc

WIDTH,HEIGHT=1440,960

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
screen.fill(pygame.Color('black'))

colors=[pygame.Color('red'),pygame.Color('green'),pygame.Color('blue'),pygame.Color('yellow'),pygame.Color('magenta'),pygame.Color('cyan')]
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
NUMBER_OF_PARTICLES=20
NUMBER_OF_FIREWORKS=30

@jit(nopython=True, parallel=True)
def calculate_particle_positions(start, end, progress):
    """Calculate particle positions at a given progress (0.0 to 1.0)"""
    x_local = np.zeros(NUMBER_OF_PARTICLES, dtype=np.int32)
    y_local = np.zeros(NUMBER_OF_PARTICLES, dtype=np.int32)
    speeds = np.zeros(NUMBER_OF_PARTICLES, dtype=np.float64)
    
    # Each particle has a different max speed
    for i in prange(NUMBER_OF_PARTICLES):
        speeds[i] = np.random.random()
    
    # Calculate positions based on progress and individual speeds
    for i in prange(NUMBER_OF_PARTICLES):
        speed_factor = speeds[i] * progress
        dx=(end[0]-start[0])*speed_factor
        dy=(end[1]-start[1])*speed_factor
        x_local[i]=np.int32(start[0]+dx)
        y_local[i]=np.int32(start[1]+dy)
    
    return x_local, y_local

def draw_particles(pixels, x_positions, y_positions, color):
    """Draw particles at given positions"""
    for i in range(NUMBER_OF_PARTICLES):
        x, y = x_positions[i], y_positions[i]
        if x>=0 and x<WIDTH and y>=0 and y<HEIGHT:
            pixels[x,y]=color

class Firework:
    """Represents a single firework with its properties"""
    def __init__(self, xc, yc, radius):
        self.xc = xc
        self.yc = yc
        self.radius = radius
        self.color = random.choice(colors)
        self.color_rgb = (self.color.r, self.color.g, self.color.b)
        
        # Calculate end points for all rays
        self.end_points = []
        for angle in range(0, 360, 5+random.randint(0,30)):
            xs = np.int32(xc + math.cos(math.radians(angle)) * radius)
            ys = np.int32(yc + math.sin(math.radians(angle)) * radius)
            self.end_points.append((xs, ys))
    
    def draw_at_progress(self, pixels, progress):
        """Draw this firework at a given progress level"""
        for end_point in self.end_points:
            x_pos, y_pos = calculate_particle_positions((self.xc, self.yc), end_point, progress)
            draw_particles(pixels, x_pos, y_pos, self.color_rgb)

def draw_fireworks(num_frames=60):
    """Draw all fireworks in parallel over multiple frames"""
    # Create all fireworks upfront
    fireworks = []
    for i in range(NUMBER_OF_FIREWORKS):
        fw = Firework(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(100, 200))
        fireworks.append(fw)
    
    # Animate all fireworks together
    for frame in range(num_frames):
        progress = (frame + 1) / num_frames
        screen.fill((0, 0, 0))  # Clear screen each frame
        pixels = pygame.surfarray.pixels3d(screen)
        
        # Draw all fireworks at current progress
        for fw in fireworks:
            fw.draw_at_progress(pixels, progress)
        
        del pixels
        gc.collect()
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

def main():
    global WIDTH,HEIGHT
    while True :
        draw_fireworks()
        text = font.render('HAPPY NEW YEAR 2026!', True, (255, 255, 255))

        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WIDTH,HEIGHT = event.w,event.h
                screen.fill(pygame.Color('black'))
        #wait for 2 seconds
        pygame.time.wait(2000)
        screen.fill(pygame.Color('black'))
if __name__ == '__main__':
    main()