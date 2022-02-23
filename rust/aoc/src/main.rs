use std::fs::File;
use std::io::{self, BufRead};

fn day_1() {
    let mut result: u32 = 0;
    let mut current;  
    let mut prev=0; 
    // open file
    let file= File::open("./input.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

    for (index,line) in lines.enumerate() {
        let line = line.unwrap();
        current = line.parse::<u32>().unwrap();
        if index > 0 {
            let diff = current as i32 - prev as i32;
            //println!("{}, {}", diff, index);
            if diff > 0 { result+=1; }
        }
        prev = current;
    }
    println!("{}", result);
}

fn day_1b() {
    let mut result: u32 = 0;
    let file= File::open("./test2.txt").unwrap();
    let lines = io::BufReader::new(file).lines();
    let mut current;  
    let mut prev=0; 
    for (index,line) in lines.enumerate() {
        if i<3 {
            sum = sum + current;
        }
    }
}

fn main() {
    day_1b();
}