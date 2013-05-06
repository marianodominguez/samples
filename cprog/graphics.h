
int openWindow(int x, int y , int w, int h, int colors);
int fullscreenMode(int x, int y , int w, int h, int colors);
void putPixelColor(int x, int y, int color);
void putPixel(int x, int y);
void setColor(int color, int ncolor);
void setColor(unsigned short r, unsigned short g, unsigned short b, int ncolor);
void drawTo(int x, int y);
void drawToColor(int x, int y, int color);
void drawLine(int x, int y);
void drawLineColor(int x, int y, int color);

