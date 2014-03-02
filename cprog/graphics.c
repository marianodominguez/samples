#include <stdlib.h>
#include <math.h>
#include "SDL/SDL.h"
#include "graphics.h"

SDL_Surface *screen;

void _drawPixel(Uint8 R, Uint8 G, Uint8 B, int x, int y, int update)
{
    Uint32 color = SDL_MapRGB(screen->format, R, G, B);

    if ( SDL_MUSTLOCK(screen)) {
        if ( SDL_LockSurface(screen) < 0 ) {
            return;
        }
    }
    switch (screen->format->BytesPerPixel) {
        case 1: { /* Assuming 8-bpp */
            Uint8 *bufp;

            bufp = (Uint8 *)screen->pixels + y*screen->pitch + x;
            *bufp = color;
        }
        break;

        case 2: { /* Probably 15-bpp or 16-bpp */
            Uint16 *bufp;

            bufp = (Uint16 *)screen->pixels + y*screen->pitch/2 + x;
            *bufp = color;
        }
        break;

        case 3: { /* Slow 24-bpp mode, usually not used */
            Uint8 *bufp;

            bufp = (Uint8 *)screen->pixels + y*screen->pitch + x;
            *(bufp+screen->format->Rshift/8) = R;
            *(bufp+screen->format->Gshift/8) = G;
            *(bufp+screen->format->Bshift/8) = B;
        }
        break;

        case 4: { /* Probably 32-bpp */
            Uint32 *bufp;

            bufp = (Uint32 *)screen->pixels + y*screen->pitch/4 + x;
            *bufp = color;
        }
        break;
    }
    if ( SDL_MUSTLOCK(screen)) {
        SDL_UnlockSurface(screen);
    }
    if (update) SDL_UpdateRect(screen, x, y, 1, 1);
}


int openWindow(int x, int y , int w, int h, int colors) {

    if ( SDL_Init(SDL_INIT_AUDIO|SDL_INIT_VIDEO) < 0 ) {
        fprintf(stderr, "Unable to init SDL: %s\n", SDL_GetError());
        return 1;
    }

    screen = SDL_SetVideoMode(x, y, colors, SDL_SWSURFACE);
    if ( screen == NULL ) {
        fprintf(stderr, "Unable to set video: %s\n", SDL_GetError());
        return 1;
    }

    return 0;
}

int fullscreenMode(int x, int y , int w, int h, int colors) {
    if ( SDL_Init(SDL_INIT_AUDIO|SDL_INIT_VIDEO) < 0 ) {
        fprintf(stderr, "Unable to init SDL: %s\n", SDL_GetError());
        return 1;
    }

    screen = SDL_SetVideoMode(x, y, colors, SDL_SWSURFACE|SDL_FULLSCREEN);
    if ( screen == NULL ) {
        fprintf(stderr, "Unable to set video: %s\n", SDL_GetError());
        return 1;
    }

    return 0;
}

void putPixelColor(int x, int y, int color) {
        _drawPixel(screen,R,G,B,x,y,1);
}

void putPixel(int x, int y) {

        _drawPixel(screen,R,G,B,x,y,1);
}

void setColor(int color, int ncolor);
void setColor(unsigned short r, unsigned short g, unsigned short b, int ncolor);
void drawTo(int x, int y);
void drawToColor(int x, int y, int color);
void drawLine(int x, int y);
void drawLineColor(int x, int y, int color);

