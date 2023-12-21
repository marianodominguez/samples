#include <allegro5/allegro5.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_primitives.h>
#include <stdbool.h>

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float r1=60,r2=-50,ph=0,th=0;

void draw() {

    float x,y,x1,y1;
    for (int i=0; i<300; i++) {
        x=r1*sin(th)+r2*sin(ph);
        y=r1*cos(th)+r2*cos(ph);
        if(i==0) {
            x1=x;
            y1=y;
        } else {
            al_draw_line(x+400,y+300,x1+400,y1+300, al_map_rgb(255, 120, 255), 0);
            x1=x;
            y1=y;
        }
        th+=M_PI/17;
        ph+=M_PI/23;
    }
}

int main() {
    al_init();
    al_install_keyboard();
    al_init_primitives_addon();

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

        al_wait_for_event(queue, &event);

        if(event.type == ALLEGRO_EVENT_TIMER)
            redraw = true;
        else if( (event.type == ALLEGRO_EVENT_DISPLAY_CLOSE))
            break;

        if(redraw && al_is_event_queue_empty(queue))
        {
            al_clear_to_color(al_map_rgb(0, 0, 0));
            al_draw_text(font, al_map_rgb(255, 255, 255), 0, 0, 0, "2d shapes");

            draw();
            ph=0;
            th=0;
            r1+=1;
            //r2+=1;

            if (r1>100) {
                r1=0;
                r2+=1;
            }
            if (r2>50) r2=-50;

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
