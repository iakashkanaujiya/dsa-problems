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
        let mut intervals: Vec<Vec<i32>> = Vec::new();
        loop {
            let _line = read_line();
            if _line.trim().is_empty() { break; }
            intervals.push(_line.split_whitespace().map(|x| x.parse().unwrap()).collect());
        }
        let result = Solution::merge(intervals);
        for _row in &result {
            let _strs: Vec<String> = _row.iter().map(|x| x.to_string()).collect();
            println!("{}", _strs.join(" "));
        }
    }
}
