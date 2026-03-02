##USER_CODE##

fn main() {
    use std::io::{self, BufRead};
    let stdin = io::stdin();
    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());
    let mut read_line = || lines_iter.next().unwrap_or_default();
    let s: String = read_line().trim().to_string();
    let result = Solution::longestValidParentheses(s);
    println!("{}", result);
}
