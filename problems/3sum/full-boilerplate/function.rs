##USER_CODE##

fn main() {
    use std::io::{self, BufRead};
    let stdin = io::stdin();
    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());
    let mut read_line = || lines_iter.next().unwrap_or_default();
    let nums: Vec<i32> = read_line().split_whitespace()
        .map(|x| x.parse().unwrap()).collect();
    let result = Solution::threeSum(nums);
    for _row in &result {
        let _strs: Vec<String> = _row.iter().map(|x| x.to_string()).collect();
        println!("{}", _strs.join(" "));
    }
}
