
#include <allegro5/allegro5.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_primitives.h>
#include <stdbool.h>

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N_VERTICES 3488*3

const int nvert=4;
const int nfaces=6;
unsigned int idx;
unsigned int screen,row,col;
float th=-2*M_PI;

float Mx[N_VERTICES],My[N_VERTICES], Mz[N_VERTICES];

void read_model(char *fn) {
    char tmpx[12],tmpy[12],tmpz[12];
    char nv[5], line[255];
    FILE* f=fopen(fn, "r");
    if (f==NULL) {
        printf("Unable to read model");
        exit(1);
    }
    fgets(nv, sizeof(nv),f );
    if (atoi(nv)*3 != N_VERTICES) {
        printf("Invalid model, wrong number of vertices");
        exit(1);
    }

    for(int i=0;i<N_VERTICES; i++) {
        fgets(line,sizeof(line),f);
        if (strlen(line) <= 10)
            fgets(line,sizeof(line),f);
        sscanf(line,"%s %s %s",tmpx,tmpy,tmpz);
        Mx[i]=atof(tmpx);
        My[i]=atof(tmpy);
        Mz[i]=atof(tmpz);
        //printf("%f %f %f\n",Mx[i],My[i],Mz[i]);
    }
}

void put_pixel(unsigned int x, unsigned int y) {
   al_draw_pixel(x, y,al_map_rgb(255, 255, 255)) ;
}

void line(unsigned int x, unsigned int y, unsigned int x1, unsigned int y1) {
    int x0=x;
    int y0=y;
    int dx=abs(x1-x0);
    int dy=abs(y1-y0);
    int sx = -1;
    int sy = -1;
    int rx=x1;
    int ry=y1;
    int e2,error;

    if (x0<x1) {
        sx=1;
        rx=x0;
    }
    if (y0<y1) {
        sy=1;
        ry=y0;
    }

    error = dx - dy;

    while(x0!=x1 || y0!=y1) {
        put_pixel(x0,y0);
        e2=2*error;
        if(e2 > -dy) {
            error-= dy;
            x0 += sx;
        }
        if(e2 < dx) {
            error+= dx;
            y0 += sy;
        }
    }
}

int draw(void) {
    float x,y,z,xp,yp,yr,zr;
    unsigned int i,j,xs,ys,x1,y1,x0,y0;
    float sqrt2=1.414;
    float sqrt6=2.449;
    unsigned int r = 80;
	idx=0;
	al_clear_to_color(al_map_rgb(0, 0, 0));

	for(i=0;i< N_VERTICES/3 ;i++) {
		for(j=0; j<3; j++) {
			x=Mx[idx]*100;
			y=My[idx]*100;
			z=Mz[idx]*100;
            idx++;
			//rotation
			yr =  ((long) y*cos(th)  - (long) z*sin(th));
			zr =  ((long) y*sin(th)  + (long) z*cos(th));
			xp = (long) (x-zr)/sqrt2;
			yp = (long) (x+2*yr+zr)/sqrt6;

			xs = xp + 800/2;
			ys = yp + 600/2;

			if (j==0) {
				x0=xs;
				y0=ys;
                x1=xs;
                y1=ys;
			}
			else {
				//bline(x1,y1,xs,ys);
                line(x1,y1,xs,ys);
			}
			x1=xs;
			y1=ys;
		}
        line(x0,y0,xs,ys);
     }
    return EXIT_SUCCESS;
}

int main()
{
    al_init();
    al_install_keyboard();
    al_init_primitives_addon();
    read_model("models/teapot.dta");

    ALLEGRO_TIMER* timer = al_create_timer(1.0 / 10.0);
    ALLEGRO_EVENT_QUEUE* queue = al_create_event_queue();
    ALLEGRO_DISPLAY* disp = al_create_display(800, 600);
    ALLEGRO_FONT* font = al_create_builtin_font();

    al_register_event_source(queue, al_get_keyboard_event_source());
    al_register_event_source(queue, al_get_display_event_source(disp));
    al_register_event_source(queue, al_get_timer_event_source(timer));

    bool redraw = true;
    ALLEGRO_EVENT event;

    al_start_timer(timer);
    while(1)
    {
		th= th + M_PI/20;
		if(th>=2*M_PI) th=-2*M_PI;

        al_wait_for_event(queue, &event);

        if(event.type == ALLEGRO_EVENT_TIMER)
            redraw = true;
        else if( (event.type == ALLEGRO_EVENT_DISPLAY_CLOSE))
            break;

        if(redraw && al_is_event_queue_empty(queue))
        {
            al_clear_to_color(al_map_rgb(0, 0, 0));
            al_draw_text(font, al_map_rgb(255, 255, 255), 0, 0, 0, "3D cube");

            draw();
            al_flip_display();

            redraw = false;
        }
    }

    al_destroy_font(font);
    al_destroy_display(disp);
    al_destroy_timer(timer);
    al_destroy_event_queue(queue);

    return 0;
}
