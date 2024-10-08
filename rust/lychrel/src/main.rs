fn ispalindrome(n:u64) -> bool {
    let num_as_string = n.to_string();
    let mut inv = n.to_string();
    inv.chars().rev().collect();
    inv == num_as_string
}

fn main() {
    println!("{}", ispalindrome(123321))
}
