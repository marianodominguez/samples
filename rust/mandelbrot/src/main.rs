extern crate sdl2;
extern crate num;

use sdl2::pixels::Color;
use sdl2::event::Event;
use sdl2::keyboard::Keycode;
use std::time::Duration;
use num::complex::Complex;
use sdl2::rect::Point;
use sdl2::render::WindowCanvas;


fn draw_pixel(canvas: &mut WindowCanvas,x:u32,y:u32, v:f32 ) {
    if v<0.5 { 
        canvas.set_draw_color(Color::RGB(v as u8 * 200  , 100, 100));
        canvas.draw_point(Point::new(x as i32,y as i32));
    }

    //canvas.present();
    
}

pub fn main() {
    let xmax=1.0;
    let ymax=1.5;
    let xmin=-2.5;
    let ymin=-1.5;
    let w=800;
    let h=600;

    let sdl_context = sdl2::init().unwrap();
    let video_subsystem = sdl_context.video().unwrap();

    let window = video_subsystem.window("Mandelbrot set", w, h)
        .position_centered()
        .build()
        .unwrap();
    let mut canvas=window.into_canvas().build().unwrap();
    
    canvas.set_draw_color(Color::RGB(0, 0, 0));
    canvas.clear();
    canvas.present();

    let iterations=1000;
    let mut x=xmin;
    let mut y=ymin;
    let dx=(xmax-xmin) / w as f32;
    let dy=(ymax-ymin) / h as f32;
    let mut z=Complex::new(0.0, 0.0);
    let mut c=Complex::new(0.0, 0.0);
    let mut k;

    for i in 0..w {
        for j in 0..h {
            k=0;
            z=Complex::new(0.0, 0.0);
            c=Complex::new(x, y);
            let mut v=0.0;
            while k<iterations && v<4.0 {
                z=z*z+c;
                v=z.norm();
                k+=1;
            }
            y=y+dy;
            draw_pixel(&mut canvas,i,j,v);
            //println!("{},{} = {}",x,y,v)
            // process event
        }
        x=x+dx;
        y=ymin;
        canvas.present();
    }
    
    let mut event_pump = sdl_context.event_pump().unwrap();
    'running: loop {
        for event in event_pump.poll_iter() {
            match event {
                Event::Quit {..} |
                Event::KeyDown { keycode: Some(Keycode::Escape), .. } => {
                    break 'running
                },
                _ => {}
            }
        }
        // The rest of the game loop goes here...

        canvas.present();
        ::std::thread::sleep(Duration::new(0, 1_000_000_000u32 / 60));
    }

}
