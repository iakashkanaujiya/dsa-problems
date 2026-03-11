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
        let nums1: Vec<i32> = read_line().split_whitespace()
            .map(|x| x.parse().unwrap()).collect();
        let m: i32 = read_line().trim().parse().unwrap();
        let nums2: Vec<i32> = read_line().split_whitespace()
            .map(|x| x.parse().unwrap()).collect();
        let n: i32 = read_line().trim().parse().unwrap();
        let result = Solution::merge(nums1, m, nums2, n);
        let _strs: Vec<String> = result.iter().map(|x| x.to_string()).collect();
        println!("{}", _strs.join(" "));
    }
}
