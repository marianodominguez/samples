#!/usr/bin/env python3
"""
Moire Pattern Generator

A moire pattern is an interference effect that occurs when two periodic patterns
(grids, lines, or textures) with slightly different frequencies or orientations
are superimposed. The resulting pattern shows enhanced contrast and alternating
regions of light and dark—a phenomenon widely used in textile design, printing,
and optical art.

ALGORITHM OVERVIEW:
-------------------
This implementation creates a moire pattern by radiating alternating black and
white lines from the center point (w/2, h/2) to the screen edges.

HOW IT WORKS:
1. Lines are drawn radially outward from the screen center
2. Adjacent lines alternate between black and white
3. The step size (stride) of 2 pixels determines the line spacing
4. When these radial lines overlap, interference creates the moire effect
5. The human eye perceives illusory curves and hyperbolic patterns
6. Moving/resizing creates animated moire effects

KEY PARAMETERS:
---------------
- w, h: Screen dimensions (larger = finer pattern detail)
- Step size (currently 2): Distance between adjacent lines
  * Smaller step = denser lines = more pronounced effect
  * Larger step = sparser lines = simpler pattern
- Color alternation: Black/white creates maximum contrast
- Radial geometry: Lines emanate from center point

WHAT YOU'LL SEE:
----------------
- Radiating straight lines create an illusion of curved or twisted surfaces
- Areas where line density changes show wavy interference bands
- The human visual system exaggerates small pattern differences
- Resizing the window animates the pattern in real-time
"""

import pygame
import sys

w, h = 1440, 960

black = pygame.Color('black')
white = pygame.Color('white')


def draw_moire():
  """
  Generate and render a radial moire pattern.
    
  Algorithm:
  1. Draw alternating black/white lines from center (w/2, h/2) to top/bottom edges
  2. Draw alternating black/white lines from center (w/2, h/2) to left/right edges
  3. The alternation (step of 2) combined with radial geometry creates interference
    
  Performance Note:
  - Updates display after each pair of lines (animated rendering)
  - For smooth rendering, consider buffering all lines before final update
  """
  y = 0
    
  # Draw horizontal-spanning radial lines (from center to top and bottom)
  for x in range(0, w, 2):
    pygame.draw.line(screen, black, (w / 2, h / 2), (x, 0))
    pygame.draw.line(screen, white, (w / 2, h / 2), (x + 1, 0))
    pygame.draw.line(screen, black, (w / 2, h / 2), (x, h))
    pygame.draw.line(screen, white, (w / 2, h / 2), (x + 1, h))
        
    # Draw vertical-spanning radial lines (from center to left and right)
    if y < h:
      pygame.draw.line(screen, black, (w / 2, h / 2), (0, y))
      pygame.draw.line(screen, white, (w / 2, h / 2), (0, y + 1))
      pygame.draw.line(screen, black, (w / 2, h / 2), (w, y))
      pygame.draw.line(screen, white, (w / 2, h / 2), (w, y + 1))
        
    y += 2
    pygame.display.update()
    pygame.event.get()  # Process events to keep window responsive


pygame.init()
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption('Moire Pattern Generator')
screen.fill(black)
draw_moire()

# Debounce settings: hold drawing until resizing has finished
RESIZE_DEBOUNCE_MS = 250
resizing = False
last_resize_time = 0

# Main event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            # Update sizes and recreate display surface
            w, h = event.w, event.h
            # screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
            screen.fill(black)
            # Mark that a resize is in progress and record the time
            resizing = True
            last_resize_time = pygame.time.get_ticks()

    # If a resize was happening and no new resize events arrived for the debounce
    # period, perform the (relatively expensive) redraw once.
    if resizing and (pygame.time.get_ticks() - last_resize_time) > RESIZE_DEBOUNCE_MS:
        draw_moire()
        resizing = False

    # Small delay to avoid busy-looping and to keep the UI responsive
    pygame.time.delay(10)
