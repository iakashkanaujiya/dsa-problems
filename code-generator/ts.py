import json
import os
import sys


def get_ts_type(type_str):
    mapping = {
        "int": "number",
        "float": "number",
        "double": "number",
        "bool": "boolean",
        "string": "string",
        "int[]": "number[]",
        "float[]": "number[]",
        "double[]": "number[]",
        "bool[]": "boolean[]",
        "string[]": "string[]",
        "int[][]": "number[][]",
        "float[][]": "number[][]",
        "double[][]": "number[][]",
        "bool[][]": "boolean[][]",
        "string[][]": "string[][]",
        "ListNode": "ListNode | null",
        "TreeNode": "TreeNode | null",
    }
    return mapping.get(type_str, "any")


def get_ts_read_logic(type_str, var_name):
    ts_type = get_ts_type(type_str)
    if type_str in ["int", "float", "double"]:
        return f"        const {var_name}: {ts_type} = Number(lines[idx++]);\n"
    elif type_str == "bool":
        return f"        const {var_name}: {ts_type} = lines[idx++] === 'true';\n"
    elif type_str == "string":
        return f"        const {var_name}: {ts_type} = lines[idx++];\n"
    elif type_str in ["int[]", "float[]", "double[]"]:
        return f"        const {var_name}: {ts_type} = lines[idx] ? lines[idx].split(' ').map(Number) : []; idx++;\n"
    elif type_str == "bool[]":
        return f"        const {var_name}: {ts_type} = lines[idx] ? lines[idx].split(' ').map(x => x === 'true') : []; idx++;\n"
    elif type_str == "string[]":
        return f"        const {var_name}: {ts_type} = lines[idx] ? lines[idx].split(' ') : []; idx++;\n"
    elif type_str.endswith("[][]"):
        if type_str in ["int[][]", "float[][]", "double[][]"]:
            return f"        const {var_name}: {ts_type} = readNumber2DArray(lines[idx++]);\n"
        elif type_str == "bool[][]":
            return f"        const {var_name}: {ts_type} = readBoolean2DArray(lines[idx++]);\n"
        elif type_str == "string[][]":
            return f"        const {var_name}: {ts_type} = readString2DArray(lines[idx++]);\n"
    elif type_str == "ListNode":
        return f"        const {var_name}: {ts_type} = buildList(lines[idx] ? lines[idx].split(' ') : []); idx++;\n"
    elif type_str == "TreeNode":
        return f"        const {var_name}: {ts_type} = buildTree(lines[idx] ? lines[idx].split(' ') : []); idx++;\n"
    return f"        const {var_name}: any = lines[idx++];\n"


def get_ts_write_logic(type_str, var_name):
    if type_str in ["int", "float", "double", "string"]:
        return f"        console.log({var_name});\n"
    elif type_str == "bool":
        return f"        console.log({var_name} ? 'true' : 'false');\n"
    elif type_str.endswith("[]") and not type_str.endswith("[][]"):
        return f"        console.log({var_name}.join(' '));\n"
    elif type_str.endswith("[][]"):
        return f"        for (let row of {var_name}) console.log(row.join(' '));\n"
    elif type_str == "ListNode":
        return f"        printList({var_name});\n"
    elif type_str == "TreeNode":
        return f"        printTree({var_name});\n"
    return f"        console.log({var_name});\n"


def generate_ts(structure_file, problem_dir):
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
    ts_params = ", ".join(
        [f"{p['name']}: {get_ts_type(p['type'])}" for p in data["parameters"]]
    )
    ret_type = get_ts_type(data["returnType"])

    boilerplate = ""
    if needs_list:
        boilerplate += "/**\n * Definition for singly-linked list.\n * class ListNode {\n *     val: number\n *     next: ListNode | null\n *     constructor(val?: number, next?: ListNode | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *     }\n * }\n */\n"
    if needs_tree:
        boilerplate += "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *     val: number\n *     left: TreeNode | null\n *     right: TreeNode | null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left = (left===undefined ? null : left)\n *         this.right = (right===undefined ? null : right)\n *     }\n * }\n */\n"

    boilerplate += f"class Solution {{\n    {func_name}({ts_params}): {ret_type} {{\n        // Write your code here\n        \n    }}\n}}\n"

    with open(os.path.join(boilerplate_dir, "function.ts"), "w") as f:
        f.write(boilerplate)

    # Drivercode
    driver = "const readline = require('readline');\nconst rl = readline.createInterface({ input: process.stdin });\nconst lines: string[] = [];\nrl.on('line', (line: string) => lines.push(line.trim()));\nrl.on('close', () => {\n"

    if needs_list:
        driver += "    class ListNode { val: number; next: ListNode | null; constructor(val?: number, next?: ListNode | null) { this.val = (val===undefined ? 0 : val); this.next = (next===undefined ? null : next); } }\n    function buildList(tokens: string[]): ListNode | null { if (!tokens.length) return null; let dummy = new ListNode(); let curr = dummy; for (let t of tokens) { curr.next = new ListNode(Number(t)); curr = curr.next; } return dummy.next; }\n    function printList(head: ListNode | null) { let res: number[] = []; while (head) { res.push(head.val); head = head.next; } console.log(res.join(' ')); }\n"
    if needs_tree:
        driver += "    class TreeNode { val: number; left: TreeNode | null; right: TreeNode | null; constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) { this.val = (val===undefined ? 0 : val); this.left = (left===undefined ? null : left); this.right = (right===undefined ? null : right); } }\n    function buildTree(tokens: string[]): TreeNode | null { if (!tokens.length || tokens[0] === 'null') return null; let root = new TreeNode(Number(tokens[0])); let q: TreeNode[] = [root]; let i = 1; while (q.length && i < tokens.length) { let curr = q.shift()!; if (tokens[i] !== 'null') { curr.left = new TreeNode(Number(tokens[i])); q.push(curr.left); } i++; if (i < tokens.length && tokens[i] !== 'null') { curr.right = new TreeNode(Number(tokens[i])); q.push(curr.right); } i++; } return root; }\n    function printTree(root: TreeNode | null) { if (!root) return; let q: (TreeNode | null)[] = [root]; let res: string[] = []; while(q.length) { let curr = q.shift(); if (curr) { res.push(curr.val.toString()); q.push(curr.left); q.push(curr.right); } else { res.push('null'); } } while (res.length && res[res.length-1] === 'null') res.pop(); console.log(res.join(' ')); }\n"

    if needs_2d:
        driver += "    function readNumber2DArray(line: string): number[][] { if (!line) return []; let tokens = line.split(' '); if (!tokens.length || tokens[0] === '0') return []; let rows = Number(tokens[0]); let res: number[][] = []; let idx = 1; for (let i = 0; i < rows; i++) { let cols = Number(tokens[idx++]); let row: number[] = []; for (let j = 0; j < cols; j++) row.push(Number(tokens[idx++])); res.push(row); } return res; }\n"
        driver += "    function readBoolean2DArray(line: string): boolean[][] { if (!line) return []; let tokens = line.split(' '); if (!tokens.length || tokens[0] === '0') return []; let rows = Number(tokens[0]); let res: boolean[][] = []; let idx = 1; for (let i = 0; i < rows; i++) { let cols = Number(tokens[idx++]); let row: boolean[] = []; for (let j = 0; j < cols; j++) row.push(tokens[idx++] === 'true'); res.push(row); } return res; }\n"
        driver += "    function readString2DArray(line: string): string[][] { if (!line) return []; let tokens = line.split(' '); if (!tokens.length || tokens[0] === '0') return []; let rows = Number(tokens[0]); let res: string[][] = []; let idx = 1; for (let i = 0; i < rows; i++) { let cols = Number(tokens[idx++]); let row: string[] = []; for (let j = 0; j < cols; j++) row.push(tokens[idx++]); res.push(row); } return res; }\n"

    driver += "\n    ##USER_CODE##\n\n"
    driver += "    if (lines.length === 0) return;\n    const t: number = Number(lines[0]);\n    let idx = 1;\n    for (let _i = 0; _i < t; _i++) {\n"

    call_args = []
    for p in data["parameters"]:
        driver += get_ts_read_logic(p["type"], p["name"])
        call_args.append(p["name"])

    driver += "        const sol = new Solution();\n"
    driver += (
        f"        const result: {ret_type} = sol.{func_name}({', '.join(call_args)});\n"
    )
    driver += get_ts_write_logic(data["returnType"], "result")

    driver += "    }\n});\n"

    with open(os.path.join(driver_dir, "function.ts"), "w") as f:
        f.write(driver)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: node ts.py <structure.json> <problem_dir>")
        sys.exit(1)
    generate_ts(sys.argv[1], sys.argv[2])
