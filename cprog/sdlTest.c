#include <stdlib.h>
#include <math.h>
#include "SDL/SDL.h"

SDL_Surface *screen;

void showBMP(char *file, SDL_Surface *screen, int x, int y)
{
    SDL_Surface *image;
    SDL_Rect dest;

    /* Load the BMP file into a surface */
    image = SDL_LoadBMP(file);
    if ( image == NULL ) {
        fprintf(stderr, "Couldn't load %s: %s\n", file, SDL_GetError());
        return;
    }

    /* Blit onto the screen surface.
       The surfaces should not be locked at this point.
     */
    dest.x = x;
    dest.y = y;
    dest.w = image->w;
    dest.h = image->h;
    SDL_BlitSurface(image, NULL, screen, &dest);

    /* Update the changed portion of the screen */
    SDL_UpdateRects(screen, 1, &dest);
}

void _drawPixel(SDL_Surface *screen, Uint8 R, Uint8 G, Uint8 B, int x, int y, int update)
{
    Uint32 color = SDL_MapRGB(screen->format, R, G, B);

    if(x >= screen->w) return;
    if(y >= screen->h) return;
    if(x < 0) return;
    if(y < 0) return;
    
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

void drawPixel(SDL_Surface *screen, Uint8 R, Uint8 G, Uint8 B, int x, int y)
{
    _drawPixel(screen,R,G,B,x,y,1);
}

void drawLine(SDL_Surface *screen, Uint8 R, Uint8 G, Uint8 B, int x, int y, int x1, int y1) {

    if ( SDL_MUSTLOCK(screen)) {
        if ( SDL_LockSurface(screen) < 0 ) {
            return;
        }
    }
    
    if (x<0) x=0;
    if (y<0) y=0;
    if (x>screen->w) x=screen->w;
    if (y>screen->h) y=screen->h;
    if (x1<0) x1=0;
    if (y1<0) y1=0;
    if (x1>screen->w) x1=screen->w;
    if (y1>screen->h) y1=screen->h;
    
    int x0 = x;
    int y0 = y;
    int dx = abs(x1 - x0);
    int dy = abs(y1 - y0);
    int sx = -1;
    int sy = -1;
    int rx = x1;
    int ry = y1;
    
    if (x0 < x1) {
        sx = 1;
        rx = x0;
    }
    if (y0 < y1) {
        sy = 1;
        ry = y0;
    }
    int err = dx - dy;

    while(x0!=x1 || y0!=y1) {
        _drawPixel(screen, R, G, B, x0, y0, 0);
        int e2 = 2*err;
        if (e2 > -dy) {
            err = err - dy;
            x0 = x0 + sx;
        } 
        if (e2 < dy) {
            err = err + dx;
            y0 = y0 + sy;
        } 
    }    
    if ( SDL_MUSTLOCK(screen)) {
        SDL_UnlockSurface(screen);
    }
    int rw = dx;
    int rh = dy;
    if (rw == 0) rw=1;
    if (rh == 0) rh=1;
    SDL_UpdateRect(screen, rx, ry, rw, rh);
}

void draw_curves2(SDL_Surface *screen) {
    int x=0;
    int y=480;
    for(x=0;x<640;x+=5) {
        drawLine(screen, 255, 0, 240, 230, 1, x, y);
    }
}

void draw_curves1(SDL_Surface *screen) {
    int x=0, x1=0;
    int y=0, y1=0;
    int i=0;
    double deg = (2 * M_PI) / 360;
    for(i=-360;i<360;i++) {
        x = 100 * sin(i * deg) + 320;
        y = 100 * cos(i * deg) + 240;
        x1 = 150 * sin(i * deg) + 320;
        y1 = 150 * sin(i * deg) + 240;
        
        drawLine(screen, 255, 0, 240, x1, y1, x, y);
    }
}

void draw_curves(SDL_Surface *screen) {
    int x=0, x1=0;
    int y=0, y1=0;
    int i=0;
    double deg = (2 * M_PI) / 360;
    for(i=-360;i<360;i++) {
        x = 10 * sin(i * deg) + 320;
        y = 10 * cos(i * deg) + 240;
        x1 = 250 * sin(i * deg) + 320;
        y1 = 250 * cos(i * deg) + 240;
        
        drawLine(screen, 255, 0, 240, x1, y1, x, y);
    }
}


int main(int argc, char *argv[])
{
    Uint8 *keys;    
    SDL_Event event;

    if ( SDL_Init(SDL_INIT_AUDIO|SDL_INIT_VIDEO) < 0 ) {
        fprintf(stderr, "Unable to init SDL: %s\n", SDL_GetError());
        exit(1);
    }

    screen = SDL_SetVideoMode(640, 480, 16, SDL_SWSURFACE);
    if ( screen == NULL ) {
        fprintf(stderr, "Unable to set 640x480 video: %s\n", SDL_GetError());
        exit(1);
    }
    
    draw_curves(screen);
    
    int exit =0;
    while(!exit) {
        while ( SDL_PollEvent(&event) ) {
			if ( event.type == SDL_QUIT )
				exit = 1;
		}
		keys = SDL_GetKeyState(NULL);
                
    }
    atexit(SDL_Quit);

    return 0;
}
