##USER_CODE##

fn main() {
    use std::io::{self, BufRead};
    let stdin = io::stdin();
    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());
    let mut read_line = || lines_iter.next().unwrap_or_default();
    let t_str = read_line();
    if t_str.is_empty() { return; }
    let t: i32 = t_str.trim().parse().unwrap();
    for _ in 0..t {
        let x: i32 = read_line().trim().parse().unwrap();
        let result = Solution::isPalindrome(x);
        println!("{}", if result { "true" } else { "false" });
    }
}
