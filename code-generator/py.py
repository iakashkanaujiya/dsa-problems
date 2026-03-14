import json
import os
import sys


def get_py_type(type_str):
    mapping = {
        "int": "int",
        "float": "float",
        "double": "float",
        "bool": "bool",
        "string": "str",
        "int[]": "List[int]",
        "float[]": "List[float]",
        "double[]": "List[float]",
        "bool[]": "List[bool]",
        "string[]": "List[str]",
        "int[][]": "List[List[int]]",
        "float[][]": "List[List[float]]",
        "double[][]": "List[List[float]]",
        "bool[][]": "List[List[bool]]",
        "string[][]": "List[List[str]]",
        "ListNode": "Optional[ListNode]",
        "TreeNode": "Optional[TreeNode]",
    }
    return mapping.get(type_str, "Any")


def get_py_read_logic(type_str, var_name):
    if type_str == "int":
        return f"        {var_name} = int(lines[idx])\n        idx += 1\n"
    elif type_str in ["float", "double"]:
        return f"        {var_name} = float(lines[idx])\n        idx += 1\n"
    elif type_str == "bool":
        return f"        {var_name} = lines[idx] == 'true'\n        idx += 1\n"
    elif type_str == "string":
        return f"        {var_name} = lines[idx]\n        idx += 1\n"
    elif type_str == "int[]":
        return f"        {var_name} = list(map(int, lines[idx].split())) if lines[idx] else []\n        idx += 1\n"
    elif type_str in ["float[]", "double[]"]:
        return f"        {var_name} = list(map(float, lines[idx].split())) if lines[idx] else []\n        idx += 1\n"
    elif type_str == "bool[]":
        return f"        {var_name} = [x == 'true' for x in lines[idx].split()] if lines[idx] else []\n        idx += 1\n"
    elif type_str == "string[]":
        return f"        {var_name} = lines[idx].split() if lines[idx] else []\n        idx += 1\n"
    elif type_str.endswith("[][]"):
        _ = get_py_type(type_str[:-4])
        # Need to use helper
        if type_str == "int[][]":
            return f"        {var_name} = read_int_2d_array(lines[idx])\n        idx += 1\n"
        elif type_str in ["float[][]", "double[][]"]:
            return f"        {var_name} = read_float_2d_array(lines[idx])\n        idx += 1\n"
        elif type_str == "string[][]":
            return f"        {var_name} = read_string_2d_array(lines[idx])\n        idx += 1\n"
        elif type_str == "bool[][]":
            return f"        {var_name} = read_bool_2d_array(lines[idx])\n        idx += 1\n"
    elif type_str == "ListNode":
        return (
            f"        {var_name} = build_list(lines[idx].split())\n        idx += 1\n"
        )
    elif type_str == "TreeNode":
        return (
            f"        {var_name} = build_tree(lines[idx].split())\n        idx += 1\n"
        )
    return f"        {var_name} = lines[idx]\n        idx += 1\n"


def generate_py(structure_file, problem_dir):
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
    os.makedirs(boilerplate_dir, exist_ok=True)
    os.makedirs(driver_dir, exist_ok=True)

    # Boilerplate
    imports = "from typing import List, Optional, Any\n"
    if needs_list:
        imports += "\n# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n"
    if needs_tree:
        imports += "\n# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n"

    py_params = []
    for p in data["parameters"]:
        py_params.append(f"{p['name']}: {get_py_type(p['type'])}")

    ret_type = get_py_type(data["returnType"])
    func_name = data["functionName"]

    boilerplate = f"{imports}\nclass Solution:\n    def {func_name}(self, {', '.join(py_params)}) -> {ret_type}:\n        pass\n"

    with open(os.path.join(boilerplate_dir, "function.py"), "w") as f:
        f.write(boilerplate)

    # Drivercode
    driver = "import sys\nfrom typing import List, Optional, Any\n\n"
    if needs_list:
        driver += "class ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef build_list(tokens):\n    if not tokens: return None\n    dummy = ListNode()\n    curr = dummy\n    for t in tokens:\n        curr.next = ListNode(int(t))\n        curr = curr.next\n    return dummy.next\n\ndef print_list(head):\n    res = []\n    while head:\n        res.append(str(head.val))\n        head = head.next\n    print(' '.join(res))\n\n"
    if needs_tree:
        driver += "class TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(tokens):\n    if not tokens or tokens[0] == 'null': return None\n    root = TreeNode(int(tokens[0]))\n    q = [root]\n    i = 1\n    while q and i < len(tokens):\n        curr = q.pop(0)\n        if tokens[i] != 'null':\n            curr.left = TreeNode(int(tokens[i]))\n            q.append(curr.left)\n        i += 1\n        if i < len(tokens) and tokens[i] != 'null':\n            curr.right = TreeNode(int(tokens[i]))\n            q.append(curr.right)\n        i += 1\n    return root\n\ndef print_tree(root):\n    if not root: return\n    q = [root]\n    res = []\n    while q:\n        curr = q.pop(0)\n        if curr:\n            res.append(str(curr.val))\n            q.append(curr.left)\n            q.append(curr.right)\n        else:\n            res.append('null')\n    while res and res[-1] == 'null': res.pop()\n    print(' '.join(res))\n\n"
    if needs_2d:
        driver += "def read_int_2d_array(line):\n    tokens = line.split()\n    if not tokens or tokens[0] == '0': return []\n    rows = int(tokens[0])\n    res = []\n    idx = 1\n    for _ in range(rows):\n        cols = int(tokens[idx])\n        idx += 1\n        res.append([int(x) for x in tokens[idx:idx+cols]])\n        idx += cols\n    return res\n\n"
        driver += "def read_float_2d_array(line):\n    tokens = line.split()\n    if not tokens or tokens[0] == '0': return []\n    rows = int(tokens[0])\n    res = []\n    idx = 1\n    for _ in range(rows):\n        cols = int(tokens[idx])\n        idx += 1\n        res.append([float(x) for x in tokens[idx:idx+cols]])\n        idx += cols\n    return res\n\n"
        driver += "def read_string_2d_array(line):\n    tokens = line.split()\n    if not tokens or tokens[0] == '0': return []\n    rows = int(tokens[0])\n    res = []\n    idx = 1\n    for _ in range(rows):\n        cols = int(tokens[idx])\n        idx += 1\n        res.append(tokens[idx:idx+cols])\n        idx += cols\n    return res\n\n"
        driver += "def read_bool_2d_array(line):\n    tokens = line.split()\n    if not tokens or tokens[0] == '0': return []\n    rows = int(tokens[0])\n    res = []\n    idx = 1\n    for _ in range(rows):\n        cols = int(tokens[idx])\n        idx += 1\n        res.append([x == 'true' for x in tokens[idx:idx+cols]])\n        idx += cols\n    return res\n\n"

    driver += "##USER_CODE##\n\n"
    driver += "def main():\n    lines = sys.stdin.read().splitlines()\n    if not lines: return\n    t = int(lines[0].strip())\n    idx = 1\n    for _ in range(t):\n"

    call_args = []
    for p in data["parameters"]:
        driver += get_py_read_logic(p["type"], p["name"])
        call_args.append(p["name"])

    driver += f"        result = Solution().{func_name}({', '.join(call_args)})\n"

    # Write logic
    out_type = data["returnType"]
    if out_type in ["int", "float", "double", "bool", "string"]:
        driver += "        print(str(result).lower() if isinstance(result, bool) else result)\n"
    elif out_type.endswith("[]") and not out_type.endswith("[][]"):
        driver += "        print(' '.join(map(lambda x: str(x).lower() if isinstance(x, bool) else str(x), result)))\n"
    elif out_type.endswith("[][]"):
        driver += "        for row in result:\n            print(' '.join(map(lambda x: str(x).lower() if isinstance(x, bool) else str(x), row)))\n"
    elif out_type == "ListNode":
        driver += "        print_list(result)\n"
    elif out_type == "TreeNode":
        driver += "        print_tree(result)\n"

    driver += "\nif __name__ == '__main__':\n    main()\n"

    with open(os.path.join(driver_dir, "function.py"), "w") as f:
        f.write(driver)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python py.py <structure.json> <problem_dir>")
        sys.exit(1)
    generate_py(sys.argv[1], sys.argv[2])
