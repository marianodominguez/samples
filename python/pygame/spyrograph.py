#!/usr/bin/env python3
"""
Spirograph Generator - Mathematical Visualization

A spirograph is a geometric curve traced by a point on a circle rolling inside another circle.
This implementation uses the parametric equations of a hypocycloid with tunability.

ALGORITHM:
-----------
The spirograph is generated using parametric equations:
  x(t) = R * ((1-k)*cos(t) + l*k*cos((1-k)*t/k))
  y(t) = R * ((1-k)*sin(t) - l*k*sin((1-k)*t/k))

Where:
  R (outer_radius): Radius of the fixed outer circle
  k: Ratio of inner circle radius to outer radius (r/R)
  l: Distance ratio from the center of the rolling circle to the tracing point
  t: Parameter angle in radians, swept from 0 to 2π

PARAMETERS:
-----------
- R (outer_radius): Controls the overall size of the spirograph
  * Larger R = bigger pattern
  * Range: typically 100-500

- r (inner_radius): Radius of the circle rolling inside R
  * Ratio r/R determines the pattern complexity
  * Range: typically 10-100
  * r < R required for hypocycloid

- l (pen_distance): How far the tracing point is from the center of rolling circle
  * l = 1.0: Pen at edge of rolling circle (classic hypocycloid)
  * l < 1.0: Pen closer to center (cusps become rounded)
  * l > 1.0: Pen extends beyond rolling circle (extended patterns)
  * Range: typically 0.1-1.5

- color: RGB color for the traced curve
"""

import pygame, sys
import math

w, h = 1440, 960

pygame.init()
screen = pygame.display.set_mode((w, h))

red = pygame.Color('red')
yellow = pygame.Color('yellow')
cyan = pygame.Color('cyan')
black = pygame.Color('black')

x = 0
y = 0
n = 10000  # Number of points to plot (resolution)
px, py = -1, -1  # Previous x,y for line drawing


def print_msg(msg = 'Press number keys 1-9'):
    basicfont = pygame.font.SysFont(None, 20*w//1000)
    text = basicfont.render(msg, True, pygame.Color('cyan'), pygame.Color('black'))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery//4
    screen.fill((0,0,0))
    screen.blit(text, textrect)
    pygame.display.update()


def fn(R, t, k, l):
    """
    Parametric equation for spirograph hypocycloid.
    
    Args:
        R (float): Outer circle radius
        t (float): Parameter angle in radians
        k (float): Ratio of inner to outer radius (r/R)
        l (float): Pen distance ratio from rolling circle center
    
    Returns:
        tuple: (x, y) coordinates on the spirograph curve
    """
    x = R * ((1 - k) * math.cos(t) + l * k * math.cos((1 - k) * t / k))
    y = R * ((1 - k) * math.sin(t) - l * k * math.sin((1 - k) * t / k))
    return (x, y)

def plot(x, y, c):
    """
    Plot a point and draw a line from the previous point to this one.
    
    Args:
        x (float): X coordinate in mathematical space
        y (float): Y coordinate in mathematical space
        c (pygame.Color): Color for the line
    """
    global px, py
    # Convert from mathematical coordinates to screen coordinates
    # Screen origin is top-left; mathematical origin is center
    point = (int(x + w / 2), int(h / 2 - y))
    if (px >= 0 and py >= 0):
        pygame.draw.aaline(screen, c, (px, py), point)  # aaline = anti-aliased line
    px, py = point


def spyro(R, r, l, color):
    """
    Generate and draw a spirograph pattern.
    
    Args:
        R (float): Outer circle radius (controls overall size)
        r (float): Inner rolling circle radius (controls complexity)
        l (float): Pen distance ratio (0 < l <= 1 for standard, l > 1 for extended)
        color (pygame.Color): Color to draw the curve
    """
    global px, py
    t = 0
    k = r / R  # Pre-calculate the ratio to avoid repeated division

    # Sweep through full rotation, incrementing by 1 degree per step
    for i in range(0, n):
        t += math.radians(1)  # Convert degrees to radians
        (x, y) = fn(R, t, k, l)
        plot(x, y, color)
    px, py = -1, -1  # Reset pen position


pygame.display.set_caption('Spirographs!')

# Configuration: Each tuple is (R, r, l, color)
# Demonstrates different parameter combinations for varied visual effects
args = [
    {
    'msg':'R=320, r=65: Large outer, medium inner, complex pattern with many petals',
    # l=0.8: Pen pulled back slightly from rolling circle edge → rounded cusps
    'a':(320.0, 65.0, 0.8, pygame.Color('magenta'))
    },
    {
    'msg':'R=300, r=53: Moderate ratio (5.66:1), intricate pattern',
    # l=0.9: Pen very close to rolling circle edge
    'a':(300.0, 53.0, 0.9, red)
    },
    {
    'msg':'R=156, r=56: Smaller outer radius, more compact pattern',
    # l=0.4: Pen significantly pulled back → highly rounded, almost circular
    'a':(156.0, 56.0, 0.4, yellow)
    },
    {
    'msg':'R=200, r=48: Medium outer, smaller inner, geometric pattern',
    # l=0.9: Pen at edge
    'a':(200.0, 48.0, 0.9, cyan)
    },
    {
    'msg':'R=300, r=45: Large outer, small inner (6.67:1), many-pointed star pattern)',
    # l=0.5: Pen at center of rolling circle
    'a':(300.0, 45.0, 0.5, pygame.Color('cadetblue'))
    },
    {   
    'msg':'R=100, r=15: Small overall size (6.67:1), compact detailed pattern)',
    # l=0.9: Sharp cusps
    'a':(100.0, 15.0, 0.9, pygame.Color('gray'))
    },
    {
    'msg':'R=250, r=11: Large outer, tiny inner (22.7:1), many thin petals)',
    # l=0.9: Classic hypocycloid shape
    'a':(250.0, 11.0, 0.9, pygame.Color('magenta'))
    }
]

i = 0

screen.fill(black)
print_msg(args[0]['msg'])
spyro(*args[0]['a'])

i = 1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Press any key to advance to next spirograph
            screen.fill(black)
            print_msg(args[i]['msg'])
            spyro(*args[i]['a'])
            if i >= len(args):
                sys.exit()
            i += 1
    pygame.display.update()
