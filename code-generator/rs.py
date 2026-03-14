import json
import os
import sys


def get_rs_type(type_str):
    mapping = {
        "int": "i32",
        "float": "f32",
        "double": "f64",
        "bool": "bool",
        "string": "String",
        "int[]": "Vec<i32>",
        "float[]": "Vec<f32>",
        "double[]": "Vec<f64>",
        "bool[]": "Vec<bool>",
        "string[]": "Vec<String>",
        "int[][]": "Vec<Vec<i32>>",
        "float[][]": "Vec<Vec<f32>>",
        "double[][]": "Vec<Vec<f64>>",
        "bool[][]": "Vec<Vec<bool>>",
        "string[][]": "Vec<Vec<String>>",
        "ListNode": "Option<Box<ListNode>>",
        "TreeNode": "Option<Rc<RefCell<TreeNode>>>",
    }
    return mapping.get(type_str, "String")


def get_rs_read_logic(type_str, var_name):
    rs_type = get_rs_type(type_str)
    if type_str in ["int", "float", "double", "bool"]:
        return f"        let {var_name}: {rs_type} = read_line().trim().parse().unwrap();\n"
    elif type_str == "string":
        return f"        let {var_name}: String = read_line();\n"
    elif type_str in ["int[]", "float[]", "double[]"]:
        return f"        let {var_name}: {rs_type} = read_line().split_whitespace().map(|x| x.parse().unwrap()).collect();\n"
    elif type_str == "bool[]":
        return f'        let {var_name}: {rs_type} = read_line().split_whitespace().map(|x| x == "true").collect();\n'
    elif type_str == "string[]":
        return f"        let {var_name}: Vec<String> = read_line().split_whitespace().map(|x| x.to_string()).collect();\n"
    elif type_str.endswith("[][]"):
        if type_str in ["int[][]", "float[][]", "double[][]"]:
            return f"        let {var_name}: {rs_type} = read_number_2d_array(&read_line());\n"
    elif type_str == "ListNode":
        return f"        let {var_name}: {rs_type} = build_list(&read_line());\n"
    elif type_str == "TreeNode":
        return f"        let {var_name}: {rs_type} = build_tree(&read_line());\n"
    return f"        let {var_name}: {rs_type} = read_line();\n"


def get_rs_write_logic(type_str, var_name):
    if type_str in ["int", "float", "double", "string", "bool"]:
        return f'        println!("{{}}", {var_name});\n'
    elif type_str.endswith("[]") and not type_str.endswith("[][]"):
        return f"""        let _{var_name}_strs: Vec<String> = {var_name}.iter().map(|x| x.to_string()).collect();
        println!("{{}}", _{var_name}_strs.join(" "));\n"""
    elif type_str.endswith("[][]"):
        return f"""        for row in {var_name} {{
            let _row_strs: Vec<String> = row.iter().map(|x| x.to_string()).collect();
            println!("{{}}", _row_strs.join(" "));
        }}\n"""
    elif type_str == "ListNode":
        return f"        print_list({var_name});\n"
    elif type_str == "TreeNode":
        return f"        print_tree({var_name});\n"
    return f'        println!("{{}}", {var_name});\n'


def generate_rs(structure_file, problem_dir):
    with open(structure_file, "r") as f:
        data = json.load(f)

    needs_list = False
    needs_tree = False
    needs_2d = False
    all_types = [p["type"] for p in data["parameters"]] + [data["returnType"]]
    for t in all_types:
        if "ListNode" in t:
            needs_list = True
        if "TreeNode" in t:
            needs_tree = True
        if t.endswith("[][]"):
            needs_2d = True

    boilerplate_dir = os.path.join(problem_dir, "boilerplate")
    driver_dir = os.path.join(problem_dir, "drivercode")

    # Boilerplate
    func_name = data["functionName"]

    rs_params = ", ".join(
        [f"{p['name']}: {get_rs_type(p['type'])}" for p in data["parameters"]]
    )
    ret_type = get_rs_type(data["returnType"])

    boilerplate = ""
    if needs_list:
        boilerplate += "// Definition for singly-linked list.\n// #[derive(PartialEq, Eq, Clone, Debug)]\n// pub struct ListNode {\n//   pub val: i32,\n//   pub next: Option<Box<ListNode>>\n// }\n// impl ListNode {\n//   #[inline]\n//   fn new(val: i32) -> Self {\n//     ListNode {\n//       next: None,\n//       val\n//     }\n//   }\n// }\n"
    if needs_tree:
        boilerplate += "// Definition for a binary tree node.\n// #[derive(Debug, PartialEq, Eq)]\n// pub struct TreeNode {\n//   pub val: i32,\n//   pub left: Option<Rc<RefCell<TreeNode>>>,\n//   pub right: Option<Rc<RefCell<TreeNode>>>,\n// }\n// impl TreeNode {\n//   #[inline]\n//   pub fn new(val: i32) -> Self {\n//     TreeNode {\n//       val,\n//       left: None,\n//       right: None\n//     }\n//   }\n// }\n"

    boilerplate += f"struct Solution;\nimpl Solution {{\n    pub fn {func_name}({rs_params}) -> {ret_type} {{\n        // Write your code here\n        \n    }}\n}}\n"

    with open(os.path.join(boilerplate_dir, "function.rs"), "w") as f:
        f.write(boilerplate)

    # Drivercode
    driver = ""
    # Add imports
    if needs_tree:
        driver += "use std::rc::Rc;\nuse std::cell::RefCell;\nuse std::collections::VecDeque;\n"

    if needs_list:
        driver += '#[derive(PartialEq, Eq, Clone, Debug)]\npub struct ListNode { pub val: i32, pub next: Option<Box<ListNode>> }\nimpl ListNode { #[inline] fn new(val: i32) -> Self { ListNode { next: None, val } } }\nfn build_list(line: &str) -> Option<Box<ListNode>> { if line.is_empty() { return None; }; let mut dummy = Some(Box::new(ListNode::new(0))); let mut curr = &mut dummy; for t in line.split_whitespace() { if let Some(node) = curr { node.next = Some(Box::new(ListNode::new(t.parse().unwrap()))); curr = &mut node.next; } }; dummy.unwrap().next }\nfn print_list(mut head: Option<Box<ListNode>>) { let mut res = Vec::new(); while let Some(node) = head { res.push(node.val.to_string()); head = node.next; }; println!("{}", res.join(" ")); }\n'
    if needs_tree:
        driver += '#[derive(Debug, PartialEq, Eq)]\npub struct TreeNode { pub val: i32, pub left: Option<Rc<RefCell<TreeNode>>>, pub right: Option<Rc<RefCell<TreeNode>>> }\nimpl TreeNode { #[inline] pub fn new(val: i32) -> Self { TreeNode { val, left: None, right: None } } }\nfn build_tree(line: &str) -> Option<Rc<RefCell<TreeNode>>> { if line.is_empty() || line.starts_with("null") { return None; }; let tokens: Vec<&str> = line.split_whitespace().collect(); let root = Rc::new(RefCell::new(TreeNode::new(tokens[0].parse().unwrap()))); let mut q = VecDeque::new(); q.push_back(Rc::clone(&root)); let mut i = 1; while let Some(curr) = q.pop_front() { if i < tokens.len() && tokens[i] != "null" { let left = Rc::new(RefCell::new(TreeNode::new(tokens[i].parse().unwrap()))); curr.borrow_mut().left = Some(Rc::clone(&left)); q.push_back(left); }; i += 1; if i < tokens.len() && tokens[i] != "null" { let right = Rc::new(RefCell::new(TreeNode::new(tokens[i].parse().unwrap()))); curr.borrow_mut().right = Some(Rc::clone(&right)); q.push_back(right); }; i += 1; }; Some(root) }\nfn print_tree(root: Option<Rc<RefCell<TreeNode>>>) { if root.is_none() { println!(); return; }; let mut q = VecDeque::new(); q.push_back(root); let mut res = Vec::new(); while let Some(node_opt) = q.pop_front() { if let Some(node) = node_opt { res.push(node.borrow().val.to_string()); q.push_back(node.borrow().left.clone()); q.push_back(node.borrow().right.clone()); } else { res.push("null".to_string()); } }; while let Some(last) = res.last() { if last == "null" { res.pop(); } else { break; } }; println!("{}", res.join(" ")); }\n'

    if needs_2d:
        driver += 'fn read_number_2d_array<T: std::str::FromStr>(line: &str) -> Vec<Vec<T>> where <T as std::str::FromStr>::Err: std::fmt::Debug { if line.is_empty() { return vec![]; }; let tokens: Vec<&str> = line.split_whitespace().collect(); if tokens.is_empty() || tokens[0] == "0" { return vec![]; }; let rows: usize = tokens[0].parse().unwrap(); let mut res = Vec::with_capacity(rows); let mut idx = 1; for _ in 0..rows { let cols: usize = tokens[idx].parse().unwrap(); idx += 1; let mut row = Vec::with_capacity(cols); for _ in 0..cols { row.push(tokens[idx].parse().unwrap()); idx += 1; }; res.push(row); }; res }\n'

    driver += "##USER_CODE##\n\n"
    driver += "fn main() {\n    use std::io::{self, BufRead};\n    let stdin = io::stdin();\n    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());\n    let mut read_line = || lines_iter.next().unwrap_or_default();\n    let t_str = read_line();\n    if t_str.is_empty() { return; }\n    let t: i32 = t_str.trim().parse().unwrap();\n    for _ in 0..t {\n"

    call_args = []
    for p in data["parameters"]:
        driver += get_rs_read_logic(p["type"], p["name"])
        call_args.append(p["name"])

    driver += f"        let result = Solution::{func_name}({', '.join(call_args)});\n"
    driver += get_rs_write_logic(data["returnType"], "result")

    driver += "    }\n}\n"

    with open(os.path.join(driver_dir, "function.rs"), "w") as f:
        f.write(driver)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rs.py <structure.json> <problem_dir>")
        sys.exit(1)
    generate_rs(sys.argv[1], sys.argv[2])
