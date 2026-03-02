##USER_CODE##

fn main() {
    use std::io::{self, BufRead};
    let stdin = io::stdin();
    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());
    let mut read_line = || lines_iter.next().unwrap_or_default();
    let x: i32 = read_line().trim().parse().unwrap();
    let result = Solution::isPalindrome(x);
    println!("{}", if result { "true" } else { "false" });
}
