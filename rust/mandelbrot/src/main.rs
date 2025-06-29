extern crate sdl2;
extern crate num;

use sdl2::pixels::Color;
use sdl2::event::Event;
use sdl2::keyboard::Keycode;
use num::complex::Complex;
use sdl2::rect::Point;
use sdl2::render::WindowCanvas;
use sdl2::Sdl;
use std::process;
use std::time::Duration;

fn draw_pixel(canvas: &mut WindowCanvas,x:u32,y:u32, k:u32 , i:u32) {
    let r = 136-(k * 136/i );
    let g = 100-(k * 100/i );
    let b = 246-(k * 246/i );
    //println!("{}", i-k );

    canvas.set_draw_color(Color::RGB( r as u8 ,  g as u8, b as u8 ) );
    let result = canvas.draw_point(Point::new(x as i32,y as i32));

    match result {
        Ok(_v) => {},
        Err(e) => println!("error drawing: {:?}", e),
    }
}

fn process_input(sdl_context: &Sdl) {
    let mut event_pump = sdl_context.event_pump().unwrap();
    for event in event_pump.poll_iter() {
        match event {
            Event::Quit {..} |
            Event::KeyDown { keycode: Some(Keycode::Escape), .. } => {
                process::exit(1);
            },
            _ => {}
        }
    }
}

fn main() {
    let xmax=1.0;
    let ymax=1.5;
    let xmin=-2.5;
    let ymin=-1.5;
    const W:u32=1440;
    const H:u32=1200;

    let sdl_context = sdl2::init().unwrap();
    let video_subsystem = sdl_context.video().unwrap();

    let window = video_subsystem.window("Mandelbrot set", W, H)
        .position_centered()
        .build()
        .unwrap();
    let mut canvas=window.into_canvas().build().unwrap();
    
    canvas.set_draw_color(Color::RGB(0, 0, 0));
    canvas.clear();
    canvas.present();

    const ITERATIONS:u32=80;
    let mut x=xmin;
    let mut y=ymin;
    let dx=(xmax-xmin) / W as f32;
    let dy=(ymax-ymin) / H as f32;
    let mut k:u32;
    let mut z:Complex<f32>;
    let mut c:Complex<f32>;
    let mut v:f32;
    rayon::ThreadPoolBuilder::new().num_threads(8).build_global().unwrap();

    for i in 0..W {
        for j in 0..H {
            k=0;
            z=Complex::new(0.0, 0.0);
            c=Complex::new(x, y);
            v=0.0;
            while k<ITERATIONS && v<4.0 {
                z=z*z+c;
                v=z.norm();
                k+=1;
            }
            y=y+dy;
            draw_pixel(&mut canvas,i,j,k, ITERATIONS);
            sdl_context.event_pump().unwrap();            
        }
        x=x+dx;
        y=ymin;
        sdl_context.event_pump().unwrap();
    }
    canvas.present();

    loop {
        process_input( &sdl_context);
        ::std::thread::sleep(Duration::new(0, 1_000_000_000u32 / 60));
    }

}
