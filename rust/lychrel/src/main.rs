extern crate num;
use rayon::prelude::*;

use num_bigint::BigUint;
use num::bigint::{ToBigUint};
const MAX_ITER:u32=100000;

fn ispalindrome(n:&BigUint) -> bool {
    let num_as_string = n.to_string();
    let mut inv:String = n.to_string();
    inv = reverse_string(&inv);
    //println!("{},{}", inv, num_as_string);
    inv == num_as_string
}

fn reverse_string(s: &str) -> String {
    s.chars().rev().collect()
  }

fn main() {
    (100..10000).into_par_iter().for_each( |i| {
        let mut n:BigUint = i.to_biguint().unwrap();
        let mut iter=0;
        
        while !ispalindrome(&n) && iter<MAX_ITER{
            let mut inv:String = n.to_string();
            inv = reverse_string(&inv);
            let inv_int:BigUint=inv.parse::<BigUint>().unwrap();
            n=n+inv_int;
            iter+=1;
        }
        if iter>= MAX_ITER {
            println!("{i} possible Lychrel, {iter}")
        }
    });
}
