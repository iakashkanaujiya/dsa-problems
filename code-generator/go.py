import json
import os
import sys


def get_go_type(type_str):
    mapping = {
        "int": "int",
        "float": "float64",
        "double": "float64",
        "bool": "bool",
        "string": "string",
        "int[]": "[]int",
        "float[]": "[]float64",
        "double[]": "[]float64",
        "bool[]": "[]bool",
        "string[]": "[]string",
        "int[][]": "[][]int",
        "float[][]": "[][]float64",
        "double[][]": "[][]float64",
        "bool[][]": "[][]bool",
        "string[][]": "[][]string",
        "ListNode": "*ListNode",
        "TreeNode": "*TreeNode",
    }
    return mapping.get(type_str, "interface{}")


def get_go_read_logic(type_str, var_name):
    if type_str == "int":
        return f"        {var_name}, _ := strconv.Atoi(readLine())\n"
    elif type_str in ["float", "double"]:
        return f"        {var_name}, _ := strconv.ParseFloat(readLine(), 64)\n"
    elif type_str == "bool":
        return f"        {var_name}, _ := strconv.ParseBool(readLine())\n"
    elif type_str == "string":
        return f"        {var_name} := readLine()\n"
    elif type_str == "int[]":
        return f"""        _{var_name}_parts := strings.Fields(readLine())
        {var_name} := make([]int, len(_{var_name}_parts))
        for _i, _s := range _{var_name}_parts {{ {var_name}[_i], _ = strconv.Atoi(_s) }}\n"""
    elif type_str in ["float[]", "double[]"]:
        return f"""        _{var_name}_parts := strings.Fields(readLine())
        {var_name} := make([]float64, len(_{var_name}_parts))
        for _i, _s := range _{var_name}_parts {{ {var_name}[_i], _ = strconv.ParseFloat(_s, 64) }}\n"""
    elif type_str == "bool[]":
        return f"""        _{var_name}_parts := strings.Fields(readLine())
        {var_name} := make([]bool, len(_{var_name}_parts))
        for _i, _s := range _{var_name}_parts {{ {var_name}[_i] = _s == "true" }}\n"""
    elif type_str == "string[]":
        return f"        {var_name} := strings.Fields(readLine())\n"
    elif type_str.endswith("[][]"):
        if type_str == "int[][]":
            return f"        {var_name} := readInt2DArray(readLine())\n"
    elif type_str == "ListNode":
        return f"        {var_name} := buildList(readLine())\n"
    elif type_str == "TreeNode":
        return f"        {var_name} := buildTree(readLine())\n"
    return f"        {var_name} := readLine()\n"


def get_go_write_logic(type_str, var_name):
    if type_str in ["int", "float", "double", "bool", "string"]:
        return f"        fmt.Println({var_name})\n"
    elif type_str.endswith("[]") and not type_str.endswith("[][]"):
        return f"""        _{var_name}_strs := make([]string, len({var_name}))
        for _i, _v := range {var_name} {{ _{var_name}_strs[_i] = fmt.Sprint(_v) }}
        fmt.Println(strings.Join(_{var_name}_strs, " "))\n"""
    elif type_str.endswith("[][]"):
        return f"""        for _, row := range {var_name} {{
            _row_strs := make([]string, len(row))
            for _i, _v := range row {{ _row_strs[_i] = fmt.Sprint(_v) }}
            fmt.Println(strings.Join(_row_strs, " "))
        }}\n"""
    elif type_str == "ListNode":
        return f"        printList({var_name})\n"
    elif type_str == "TreeNode":
        return f"        printTree({var_name})\n"
    return f"        fmt.Println({var_name})\n"


def generate_go(structure_file, problem_dir):
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

    # Capitalize the function name for Export in Go? Actually Go solutions don't typically enforce Export but we can use original case.
    go_params = ", ".join(
        [f"{p['name']} {get_go_type(p['type'])}" for p in data["parameters"]]
    )
    ret_type = get_go_type(data["returnType"])

    boilerplate = ""
    if needs_list:
        boilerplate += "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\n"
    if needs_tree:
        boilerplate += "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\n"

    boilerplate += f"func {func_name}({go_params}) {ret_type} {{\n    // Write your code here\n    \n}}\n"

    with open(os.path.join(boilerplate_dir, "function.go"), "w") as f:
        f.write(boilerplate)

    # Drivercode
    driver = 'package main\n\nimport (\n    "bufio"\n    "fmt"\n    "os"\n    "strconv"\n    "strings"\n)\n\n'

    if needs_list:
        driver += 'type ListNode struct { Val int; Next *ListNode }\nfunc buildList(line string) *ListNode { if line == "" { return nil }; tokens := strings.Fields(line); dummy := &ListNode{}; curr := dummy; for _, t := range tokens { val, _ := strconv.Atoi(t); curr.Next = &ListNode{Val: val}; curr = curr.Next }; return dummy.Next }\nfunc printList(head *ListNode) { res := []string{}; for head != nil { res = append(res, strconv.Itoa(head.Val)); head = head.Next }; fmt.Println(strings.Join(res, " ")) }\n'
    if needs_tree:
        driver += 'type TreeNode struct { Val int; Left *TreeNode; Right *TreeNode }\nfunc buildTree(line string) *TreeNode { if line == "" || strings.HasPrefix(line, "null") { return nil }; tokens := strings.Fields(line); val, _ := strconv.Atoi(tokens[0]); root := &TreeNode{Val: val}; q := []*TreeNode{root}; i := 1; for len(q) > 0 && i < len(tokens) { curr := q[0]; q = q[1:]; if tokens[i] != "null" { val, _ := strconv.Atoi(tokens[i]); curr.Left = &TreeNode{Val: val}; q = append(q, curr.Left) }; i++; if i < len(tokens) && tokens[i] != "null" { val, _ := strconv.Atoi(tokens[i]); curr.Right = &TreeNode{Val: val}; q = append(q, curr.Right) }; i++ }; return root }\nfunc printTree(root *TreeNode) { if root == nil { fmt.Println(); return }; q := []*TreeNode{root}; res := []string{}; for len(q) > 0 { curr := q[0]; q = q[1:]; if curr != nil { res = append(res, strconv.Itoa(curr.Val)); q = append(q, curr.Left); q = append(q, curr.Right) } else { res = append(res, "null") } }; for len(res) > 0 && res[len(res)-1] == "null" { res = res[:len(res)-1] }; fmt.Println(strings.Join(res, " ")) }\n'

    if needs_2d:
        driver += 'func readInt2DArray(line string) [][]int { if line == "" { return [][]int{} }; tokens := strings.Fields(line); if len(tokens) == 0 || tokens[0] == "0" { return [][]int{} }; rows, _ := strconv.Atoi(tokens[0]); res := make([][]int, rows); idx := 1; for i := 0; i < rows; i++ { cols, _ := strconv.Atoi(tokens[idx]); idx++; res[i] = make([]int, cols); for j := 0; j < cols; j++ { res[i][j], _ = strconv.Atoi(tokens[idx]); idx++ } }; return res }\n'

    driver += "##USER_CODE##\n\n"
    driver += 'func main() {\n    scanner := bufio.NewScanner(os.Stdin)\n    scanner.Buffer(make([]byte, 1024*1024), 1024*1024)\n    scanner.Split(bufio.ScanLines)\n    readLine := func() string {\n        scanner.Scan()\n        return strings.TrimSpace(scanner.Text())\n    }\n    tStr := readLine()\n    if tStr == "" { return }\n    t, _ := strconv.Atoi(tStr)\n    for i := 0; i < t; i++ {\n'

    call_args = []
    for p in data["parameters"]:
        driver += get_go_read_logic(p["type"], p["name"])
        call_args.append(p["name"])

    driver += f"        result := {func_name}({', '.join(call_args)})\n"
    driver += get_go_write_logic(data["returnType"], "result")

    driver += "    }\n}\n"

    with open(os.path.join(driver_dir, "function.go"), "w") as f:
        f.write(driver)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python go.py <structure.json> <problem_dir>")
        sys.exit(1)
    generate_go(sys.argv[1], sys.argv[2])
