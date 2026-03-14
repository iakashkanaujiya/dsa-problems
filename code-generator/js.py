import json
import os
import sys


def get_js_type(type_str):
    mapping = {
        "int": "Number",
        "float": "Number",
        "double": "Number",
        "bool": "Boolean",
        "string": "String",
        "int[]": "Number[]",
        "float[]": "Number[]",
        "double[]": "Number[]",
        "bool[]": "Boolean[]",
        "string[]": "String[]",
        "int[][]": "Number[][]",
        "float[][]": "Number[][]",
        "double[][]": "Number[][]",
        "bool[][]": "Boolean[][]",
        "string[][]": "String[][]",
        "ListNode": "ListNode",
        "TreeNode": "TreeNode",
    }
    return mapping.get(type_str, "any")


def get_js_read_logic(type_str, var_name):
    if type_str in ["int", "float", "double"]:
        return f"        const {var_name} = Number(lines[idx++]);\n"
    elif type_str == "bool":
        return f"        const {var_name} = lines[idx++] === 'true';\n"
    elif type_str == "string":
        return f"        const {var_name} = lines[idx++];\n"
    elif type_str in ["int[]", "float[]", "double[]"]:
        return f"        const {var_name} = lines[idx] ? lines[idx].split(' ').map(Number) : []; idx++;\n"
    elif type_str == "bool[]":
        return f"        const {var_name} = lines[idx] ? lines[idx].split(' ').map(x => x === 'true') : []; idx++;\n"
    elif type_str == "string[]":
        return f"        const {var_name} = lines[idx] ? lines[idx].split(' ') : []; idx++;\n"
    elif type_str.endswith("[][]"):
        if type_str in ["int[][]", "float[][]", "double[][]"]:
            return f"        const {var_name} = readNumber2DArray(lines[idx++]);\n"
        elif type_str == "bool[][]":
            return f"        const {var_name} = readBoolean2DArray(lines[idx++]);\n"
        elif type_str == "string[][]":
            return f"        const {var_name} = readString2DArray(lines[idx++]);\n"
    elif type_str == "ListNode":
        return f"        const {var_name} = buildList(lines[idx] ? lines[idx].split(' ') : []); idx++;\n"
    elif type_str == "TreeNode":
        return f"        const {var_name} = buildTree(lines[idx] ? lines[idx].split(' ') : []); idx++;\n"
    return f"        const {var_name} = lines[idx++];\n"


def get_js_write_logic(type_str, var_name):
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


def generate_js(structure_file, problem_dir):
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
    js_params = ", ".join([p["name"] for p in data["parameters"]])

    boilerplate = ""
    if needs_list:
        boilerplate += "/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n"
    if needs_tree:
        boilerplate += "/**\n * Definition for a binary tree node.\n * function TreeNode(val, left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left = (left===undefined ? null : left)\n *     this.right = (right===undefined ? null : right)\n * }\n */\n"

    boilerplate += f"class Solution {{\n    {func_name}({js_params}) {{\n        // Write your code here\n        \n    }}\n}}\n"

    with open(os.path.join(boilerplate_dir, "function.js"), "w") as f:
        f.write(boilerplate)

    # Drivercode
    driver = "const readline = require('readline');\nconst rl = readline.createInterface({ input: process.stdin });\nconst lines = [];\nrl.on('line', (line) => lines.push(line.trim()));\nrl.on('close', () => {\n"

    if needs_list:
        driver += "    function ListNode(val, next) { this.val = (val===undefined ? 0 : val); this.next = (next===undefined ? null : next); }\n    function buildList(tokens) { if (!tokens.length) return null; let dummy = new ListNode(); let curr = dummy; for (let t of tokens) { curr.next = new ListNode(Number(t)); curr = curr.next; } return dummy.next; }\n    function printList(head) { let res = []; while (head) { res.push(head.val); head = head.next; } console.log(res.join(' ')); }\n"
    if needs_tree:
        driver += "    function TreeNode(val, left, right) { this.val = (val===undefined ? 0 : val); this.left = (left===undefined ? null : left); this.right = (right===undefined ? null : right); }\n    function buildTree(tokens) { if (!tokens.length || tokens[0] === 'null') return null; let root = new TreeNode(Number(tokens[0])); let q = [root]; let i = 1; while (q.length && i < tokens.length) { let curr = q.shift(); if (tokens[i] !== 'null') { curr.left = new TreeNode(Number(tokens[i])); q.push(curr.left); } i++; if (i < tokens.length && tokens[i] !== 'null') { curr.right = new TreeNode(Number(tokens[i])); q.push(curr.right); } i++; } return root; }\n    function printTree(root) { if (!root) return; let q = [root]; let res = []; while(q.length) { let curr = q.shift(); if (curr) { res.push(curr.val); q.push(curr.left); q.push(curr.right); } else { res.push('null'); } } while (res.length && res[res.length-1] === 'null') res.pop(); console.log(res.join(' ')); }\n"

    if needs_2d:
        driver += "    function readNumber2DArray(line) { if (!line) return []; let tokens = line.split(' '); if (!tokens.length || tokens[0] === '0') return []; let rows = Number(tokens[0]); let res = []; let idx = 1; for (let i = 0; i < rows; i++) { let cols = Number(tokens[idx++]); let row = []; for (let j = 0; j < cols; j++) row.push(Number(tokens[idx++])); res.push(row); } return res; }\n"
        driver += "    function readBoolean2DArray(line) { if (!line) return []; let tokens = line.split(' '); if (!tokens.length || tokens[0] === '0') return []; let rows = Number(tokens[0]); let res = []; let idx = 1; for (let i = 0; i < rows; i++) { let cols = Number(tokens[idx++]); let row = []; for (let j = 0; j < cols; j++) row.push(tokens[idx++] === 'true'); res.push(row); } return res; }\n"
        driver += "    function readString2DArray(line) { if (!line) return []; let tokens = line.split(' '); if (!tokens.length || tokens[0] === '0') return []; let rows = Number(tokens[0]); let res = []; let idx = 1; for (let i = 0; i < rows; i++) { let cols = Number(tokens[idx++]); let row = []; for (let j = 0; j < cols; j++) row.push(tokens[idx++]); res.push(row); } return res; }\n"

    driver += "\n    ##USER_CODE##\n\n"
    driver += "    if (lines.length === 0) return;\n    const t = Number(lines[0]);\n    let idx = 1;\n    for (let _i = 0; _i < t; _i++) {\n"

    call_args = []
    for p in data["parameters"]:
        driver += get_js_read_logic(p["type"], p["name"])
        call_args.append(p["name"])

    driver += "        const sol = new Solution();\n"
    driver += f"        const result = sol.{func_name}({', '.join(call_args)});\n"
    driver += get_js_write_logic(data["returnType"], "result")

    driver += "    }\n});\n"

    with open(os.path.join(driver_dir, "function.js"), "w") as f:
        f.write(driver)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: node js.py <structure.json> <problem_dir>")
        sys.exit(1)
    generate_js(sys.argv[1], sys.argv[2])
