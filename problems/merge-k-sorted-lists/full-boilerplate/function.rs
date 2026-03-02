#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {
    let mut dummy = Box::new(ListNode::new(0));
    let mut cur = &mut dummy;
    for &v in vals {
        cur.next = Some(Box::new(ListNode::new(v)));
        cur = cur.next.as_mut().unwrap();
    }
    dummy.next
}

fn print_list(mut head: Option<Box<ListNode>>) {
    let mut first = true;
    while let Some(node) = head {
        if !first { print!(" "); }
        print!("{}", node.val);
        first = false;
        head = node.next;
    }
    println!();
}

##USER_CODE##

fn main() {
    use std::io::{self, BufRead};
    let stdin = io::stdin();
    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());
    let mut read_line = || lines_iter.next().unwrap_or_default();
    let _vals0: Vec<i32> = read_line().split_whitespace()
        .map(|x| x.parse().unwrap()).collect();
    let head = build_list(&_vals0);
    let result = Solution::mergeKLists(head);
    print_list(result);
}
