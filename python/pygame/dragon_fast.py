#!/usr/bin/env python3
"""Dragon curve renderer (fixed)

This implementation uses an L-system to generate the dragon curve turn sequence
and then draws the polyline in pygame. It avoids reusing names like `w` and
`h` for both screen size and step vectors (that was the bug in the original).
"""

import pygame
import sys

# Screen size
SCREEN_W, SCREEN_H = 1440, 960

# Dragon parameters
ITERATIONS = 14   # number of production iterations for the L-system
STEP = 5          # pixel step length for each "F"
COLOR = pygame.Color('yellow')


def generate_dragon_lsystem(iterations: int) -> str:
    """Generate the dragon curve L-system string.

    Axiom: "FX"
    Rules:
      X -> X+YF+
      Y -> -FX-Y

    Only F, +, - are interpreted (X and Y are placeholders for productions).
    """
    axiom = "FX"
    rules = {
        'X': 'X+YF+',
        'Y': '-FX-Y'
    }
    s = axiom
    for _ in range(iterations):
        s = ''.join(rules.get(ch, ch) for ch in s)
    return s


def draw_dragon(surface, start_pos, step, turns, color):
    """Interpret the L-system turns and draw the curve on the surface.

    - start_pos: (x,y) starting pixel coordinates
    - step: length in pixels for each forward move 'F'
    - turns: string containing 'F', '+', '-' (plus/minus rotate 90 degrees)
    """
    x, y = start_pos
    # initial heading: to the right (dx=1, dy=0)
    dx, dy = 1, 0

    for ch in turns:
        if ch == 'F':
            nx = x + dx * step
            ny = y + dy * step
            pygame.draw.line(surface, color, (x, y), (nx, ny))
            x, y = nx, ny
        elif ch == '+':
            # rotate right 90 degrees: (dx,dy) -> (dy, -dx)
            dx, dy = dy, -dx
        elif ch == '-':
            # rotate left 90 degrees: (dx,dy) -> (-dy, dx)
            dx, dy = -dy, dx
        # ignore other symbols (X, Y) if any remain


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    screen.fill(pygame.Color('black'))

    # Generate the instruction string and draw
    instr = generate_dragon_lsystem(ITERATIONS)
    # interpret only F,+,- (X/Y are expansion symbols and will not be drawn)
    draw_dragon(screen, (SCREEN_W // 2, SCREEN_H // 2), STEP, instr, COLOR)
    pygame.display.update()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()






