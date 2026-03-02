##USER_CODE##

fn main() {
    use std::io::{self, BufRead};
    let stdin = io::stdin();
    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());
    let mut read_line = || lines_iter.next().unwrap_or_default();
    let prices: Vec<i32> = read_line().split_whitespace()
        .map(|x| x.parse().unwrap()).collect();
    let result = Solution::maxProfit(prices);
    println!("{}", result);
}
