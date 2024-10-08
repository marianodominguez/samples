fn ispalindrome(n:u64) -> bool {
    let num_as_string = n.to_string();
    let mut inv:String = n.to_string();
    inv = reverse_string(&inv);
    println!("{},{}", inv, num_as_string);
    inv == num_as_string
}

fn reverse_string(s: &str) -> String {
    s.chars().rev().collect()
  }

fn main() {
    println!("{}", ispalindrome(123321));
    println!("{}", ispalindrome(123211));
}
