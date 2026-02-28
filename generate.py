"""
================================================================
generate.py — Auto-generates boilerplate & full-boilerplate
              from a problem's structure.md

Usage:
  python generate.py Array/2sum
  python generate.py Array/3sum
================================================================
"""

import sys
import os
import json
import re

# ─── CLI ────────────────────────────────────────────────────
if len(sys.argv) < 2:
    print("Usage:   python generate.py <Category/ProblemName>")
    print("Example: python generate.py Array/2sum")
    sys.exit(1)

problem = sys.argv[1]

base_dir = os.path.dirname(os.path.abspath(__file__))
problem_dir = os.path.join(base_dir, "problems", problem.replace("/", os.sep))
structure_file = os.path.join(problem_dir, "structure.md")
boilerplate_dir = os.path.join(problem_dir, "boilerplate")
full_boilerplate_dir = os.path.join(problem_dir, "full-boilerplate")

if not os.path.exists(structure_file):
    print(f"ERROR: structure.md not found at {structure_file}")
    sys.exit(1)

# ─── Parse structure.md — extract the JSON block ────────────
with open(structure_file, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"```json\s*([\s\S]*?)\s*```", content)
if not match:
    print("ERROR: No ```json block found in structure.md")
    sys.exit(1)

try:
    schema = json.loads(match.group(1))
except json.JSONDecodeError as e:
    print(f"ERROR: Invalid JSON in structure.md: {e}")
    sys.exit(1)

function_name = schema["functionName"]
parameters = schema["parameters"]
return_type = schema["returnType"]
input_format = schema["inputFormat"]
output_format = schema["outputFormat"]

# ─── Type Maps ───────────────────────────────────────────────
CPP_TYPES = {
    "int": "int",
    "int[]": "vector<int>",
    "int[][]": "vector<vector<int>>",
    "long": "long long",
    "long[]": "vector<long long>",
    "string": "string",
    "string[]": "vector<string>",
    "bool": "bool",
    "double": "double",
    "float": "float",
    "void": "void",
    "ListNode": "ListNode*",
}

PY_TYPES = {
    "int": "int",
    "int[]": "List[int]",
    "int[][]": "List[List[int]]",
    "long": "int",
    "long[]": "List[int]",
    "string": "str",
    "string[]": "List[str]",
    "bool": "bool",
    "double": "float",
    "float": "float",
    "void": "None",
    "ListNode": "Optional[ListNode]",
}

JS_TYPES = {
    "int": "number",
    "int[]": "number[]",
    "int[][]": "number[][]",
    "long": "number",
    "long[]": "number[]",
    "string": "string",
    "string[]": "string[]",
    "bool": "boolean",
    "double": "number",
    "float": "number",
    "void": "void",
    "ListNode": "ListNode",
}


def cpp_type(t):
    return CPP_TYPES.get(t, t)


def py_type(t):
    return PY_TYPES.get(t, t)


def js_type(t):
    return JS_TYPES.get(t, t)


# ─── Detect if problem uses ListNode ─────────────────────────
def uses_list_node():
    types = [p["type"] for p in parameters] + [return_type]
    return "ListNode" in types


# ─── ListNode preambles ──────────────────────────────────────
CPP_LISTNODE_PREAMBLE = """\
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

// Build linked list from a vector of values
ListNode* buildList(const vector<int>& vals) {
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int v : vals) { cur->next = new ListNode(v); cur = cur->next; }
    return dummy.next;
}

// Serialize linked list to space-separated string
void printList(ListNode* head) {
    bool first = true;
    while (head) {
        if (!first) cout << " ";
        cout << head->val;
        first = false;
        head = head->next;
    }
    cout << "\\n";
}
"""

JS_LISTNODE_PREAMBLE = """\
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(arr) {
  let dummy = new ListNode(0);
  let cur = dummy;
  for (const v of arr) { cur.next = new ListNode(v); cur = cur.next; }
  return dummy.next;
}

function printList(head) {
  const vals = [];
  while (head) { vals.push(head.val); head = head.next; }
  console.log(vals.join(" "));
}
"""

PY_LISTNODE_PREAMBLE = """\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" ".join(vals))
"""


# ─── C++ Input Parser ────────────────────────────────────────
def cpp_parse_input():
    lines = []
    for i, f in enumerate(input_format):
        field, typ = f["field"], f["type"]
        if typ in ("int[]", "long[]"):
            vec_type = "long long" if typ == "long[]" else "int"
            lines.append(f"    string _line{i}; getline(cin, _line{i});")
            lines.append(f"    istringstream _iss{i}(_line{i});")
            lines.append(
                f"    {cpp_type(typ)} {field}; {{ {vec_type} _v; while(_iss{i} >> _v) {field}.push_back(_v); }}"
            )
        elif typ == "int[][]":
            lines.append(f"    {cpp_type(typ)} {field};")
            lines.append(
                f"    {{ string _row; while(getline(cin, _row) && !_row.empty()) {{"
            )
            lines.append(f"        istringstream _rs(_row); vector<int> _r; int _v;")
            lines.append(f"        while(_rs >> _v) _r.push_back(_v);")
            lines.append(f"        {field}.push_back(_r); }} }}")
        elif typ == "string[]":
            lines.append(f"    string _line{i}; getline(cin, _line{i});")
            lines.append(f"    istringstream _iss{i}(_line{i});")
            lines.append(
                f"    vector<string> {field}; {{ string _v; while(_iss{i} >> _v) {field}.push_back(_v); }}"
            )
        elif typ == "string":
            lines.append(f"    string {field}; getline(cin, {field});")
        elif typ == "bool":
            lines.append(
                f"    bool {field}; {{ int _b; cin >> _b; {field} = _b; cin.ignore(); }}"
            )
        elif typ == "ListNode":
            lines.append(f"    string _line{i}; getline(cin, _line{i});")
            lines.append(f"    istringstream _iss{i}(_line{i});")
            lines.append(
                f"    vector<int> _vals{i}; {{ int _v; while(_iss{i} >> _v) _vals{i}.push_back(_v); }}"
            )
            lines.append(f"    ListNode* {field} = buildList(_vals{i});")
        else:
            lines.append(f"    {cpp_type(typ)} {field}; cin >> {field}; cin.ignore();")
    return "\n".join(lines)


# ─── C++ Output Printer ──────────────────────────────────────
def cpp_print_output(ret_var):
    out = output_format[0]
    typ = out["type"]
    delim = out.get("delimiter", " ")
    if delim == "\n":
        delim = "\\n"
    if typ in ("int[]", "long[]", "string[]"):
        return (
            f"    for (int i = 0; i < (int){ret_var}.size(); i++) {{\n"
            f'        if (i) cout << "{delim}";\n'
            f"        cout << {ret_var}[i];\n"
            f"    }}\n"
            f'    cout << "\\n";'
        )
    elif typ == "int[][]":
        return (
            f"    for (auto& row : {ret_var}) {{\n"
            f"        for (int i = 0; i < (int)row.size(); i++) {{\n"
            f'            if (i) cout << "{delim}";\n'
            f"            cout << row[i];\n"
            f"        }}\n"
            f'        cout << "\\n";\n'
            f"    }}"
        )
    elif typ == "ListNode":
        return f"    printList({ret_var});"
    elif typ == "bool":
        return f'    cout << ({ret_var} ? "true" : "false") << "\\n";'
    elif typ == "void":
        return ""
    else:
        return f'    cout << {ret_var} << "\\n";'


# ─── JS Input Parser ─────────────────────────────────────────
def js_parse_input():
    lines = []
    for i, f in enumerate(input_format):
        field, typ = f["field"], f["type"]
        if typ in ("int[]", "long[]"):
            lines.append(f'  const {field} = lines[{i}].split(" ").map(Number);')
        elif typ == "int[][]":
            lines.append(
                f'  const {field} = lines.slice({i}).filter(l => l !== "").map(l => l.split(" ").map(Number));'
            )
        elif typ == "string[]":
            lines.append(f'  const {field} = lines[{i}].split(" ");')
        elif typ == "string":
            lines.append(f"  const {field} = lines[{i}];")
        elif typ == "bool":
            lines.append(
                f'  const {field} = lines[{i}].trim() === "true" || lines[{i}].trim() === "1";'
            )
        elif typ == "ListNode":
            lines.append(
                f'  const {field} = buildList(lines[{i}].split(" ").map(Number));'
            )
        else:
            cast = "Number" if typ in ("int", "long", "double", "float") else ""
            lines.append(f"  const {field} = {cast}(lines[{i}]);")
    return "\n".join(lines)


# ─── JS Output Printer ───────────────────────────────────────
def js_print_output(ret_var):
    out = output_format[0]
    typ = out["type"]
    delim = out.get("delimiter", " ")
    if typ in ("int[]", "long[]", "string[]"):
        return f'  console.log({ret_var}.join("{delim}"));'
    elif typ == "int[][]":
        return f'  {ret_var}.forEach(row => console.log(row.join("{delim}")));'
    elif typ == "ListNode":
        return f"  printList({ret_var});"
    elif typ == "bool":
        return f'  console.log({ret_var} ? "true" : "false");'
    elif typ == "void":
        return ""
    else:
        return f"  console.log({ret_var});"


# ─── Python Input Parser ─────────────────────────────────────
def py_parse_input():
    lines = []
    for i, f in enumerate(input_format):
        field, typ = f["field"], f["type"]
        if typ in ("int[]", "long[]"):
            lines.append(f"    {field} = list(map(int, lines[{i}].split()))")
        elif typ == "int[][]":
            lines.append(
                f"    {field} = [list(map(int, l.split())) for l in lines[{i}:] if l.strip()]"
            )
        elif typ == "string[]":
            lines.append(f"    {field} = lines[{i}].split()")
        elif typ == "string":
            lines.append(f"    {field} = lines[{i}]")
        elif typ == "bool":
            lines.append(f'    {field} = lines[{i}].strip() in ("true", "1")')
        elif typ in ("double", "float"):
            lines.append(f"    {field} = float(lines[{i}])")
        elif typ == "ListNode":
            lines.append(
                f"    {field} = build_list(list(map(int, lines[{i}].split())))"
            )
        else:
            lines.append(f"    {field} = int(lines[{i}])")
    return "\n".join(lines)


# ─── Python Output Printer ───────────────────────────────────
def py_print_output(ret_var):
    out = output_format[0]
    typ = out["type"]
    delim = out.get("delimiter", " ")
    if typ in ("int[]", "long[]"):
        return f'    print("{delim}".join(map(str, {ret_var})))'
    elif typ == "string[]":
        return f'    print("{delim}".join({ret_var}))'
    elif typ == "int[][]":
        return (
            f'    for row in {ret_var}:\n        print("{delim}".join(map(str, row)))'
        )
    elif typ == "ListNode":
        return f"    print_list({ret_var})"
    elif typ == "bool":
        return f'    print("true" if {ret_var} else "false")'
    elif typ == "void":
        return ""
    else:
        return f"    print({ret_var})"


# ─── Generators ──────────────────────────────────────────────


def gen_cpp_boilerplate():
    def param_str(p):
        t = cpp_type(p["type"])
        is_ref = p["type"].endswith("[]") or p["type"] == "string"
        return f"{t}{chr(38) if is_ref else ''} {p['name']}"

    preamble = CPP_LISTNODE_PREAMBLE if uses_list_node() else ""
    params = ", ".join(param_str(p) for p in parameters)
    return f"{preamble}{cpp_type(return_type)} {function_name}({params}) {{\n    // Write your code here\n}}\n"


def gen_cpp_full_boilerplate():
    def param_str(p):
        t = cpp_type(p["type"])
        is_ref = p["type"].endswith("[]") or p["type"] == "string"
        return f"{t}{chr(38) if is_ref else ''} {p['name']}"

    preamble = CPP_LISTNODE_PREAMBLE if uses_list_node() else ""
    params = ", ".join(param_str(p) for p in parameters)
    call_args = ", ".join(p["name"] for p in parameters)
    ret_line = (
        f"    {cpp_type(return_type)} result = {function_name}({call_args});"
        if return_type != "void"
        else f"    {function_name}({call_args});"
    )
    print_line = cpp_print_output("result")
    return (
        f"#include <bits/stdc++.h>\n"
        f"using namespace std;\n\n"
        f"{preamble}"
        f"##USER_CODE##\n\n"
        f"int main() {{\n"
        f"    ios_base::sync_with_stdio(false);\n"
        f"    cin.tie(NULL);\n\n"
        f"{cpp_parse_input()}\n"
        f"{ret_line}\n"
        f"{print_line}\n"
        f"    return 0;\n"
        f"}}\n"
    )


def gen_js_boilerplate():
    preamble = JS_LISTNODE_PREAMBLE if uses_list_node() else ""
    jsdoc_params = "\n".join(
        f" * @param {{{js_type(p['type'])}}} {p['name']}" for p in parameters
    )
    jsdoc_return = f" * @return {{{js_type(return_type)}}}"
    param_names = ", ".join(p["name"] for p in parameters)
    return (
        f"{preamble}"
        f"/**\n{jsdoc_params}\n{jsdoc_return}\n */\n"
        f"function {function_name}({param_names}) {{\n"
        f"  // Write your code here\n"
        f"}}\n"
    )


def gen_js_full_boilerplate():
    preamble = JS_LISTNODE_PREAMBLE if uses_list_node() else ""
    param_names = ", ".join(p["name"] for p in parameters)
    call_line = (
        f"  const result = {function_name}({param_names});"
        if return_type != "void"
        else f"  {function_name}({param_names});"
    )
    print_line = js_print_output("result")
    return (
        f'const readline = require("readline");\n'
        f"const rl = readline.createInterface({{ input: process.stdin }});\n"
        f"const lines = [];\n"
        f'rl.on("line", (line) => lines.push(line.trim()));\n'
        f'rl.on("close", () => {{\n'
        f"{js_parse_input()}\n\n"
        f"{preamble}"
        f"  ##USER_CODE##\n\n"
        f"{call_line}\n"
        f"{print_line}\n"
        f"}});\n"
    )


def gen_py_boilerplate():
    has_listnode = uses_list_node()
    needs_typing = any(p["type"].endswith("[]") for p in parameters)
    preamble = PY_LISTNODE_PREAMBLE + "\n\n" if has_listnode else ""
    typing_import = (
        "from typing import List, Optional\n\n"
        if has_listnode
        else ("from typing import List\n\n" if needs_typing else "")
    )
    params = ", ".join(f"{p['name']}: {py_type(p['type'])}" for p in parameters)
    ret_py = py_type(return_type)
    return (
        f"{typing_import}"
        f"{preamble}"
        f"def {function_name}({params}) -> {ret_py}:\n"
        f"    # Write your code here\n"
        f"    pass\n"
    )


def gen_py_full_boilerplate():
    has_listnode = uses_list_node()
    needs_typing = any(
        p["type"].endswith("[]") for p in parameters
    ) or return_type.endswith("[]")
    preamble = PY_LISTNODE_PREAMBLE + "\n\n" if has_listnode else ""
    typing_import = (
        "from typing import List, Optional\n"
        if has_listnode
        else ("from typing import List\n" if needs_typing else "")
    )
    params = ", ".join(f"{p['name']}: {py_type(p['type'])}" for p in parameters)
    ret_py = py_type(return_type)
    param_names = ", ".join(p["name"] for p in parameters)
    call_line = (
        f"    result = {function_name}({param_names})"
        if return_type != "void"
        else f"    {function_name}({param_names})"
    )
    print_line = py_print_output("result")
    return (
        f"import sys\n"
        f"{typing_import}\n"
        f"{preamble}"
        f"##USER_CODE##\n\n"
        f"def main():\n"
        f"    lines = sys.stdin.read().strip().splitlines()\n"
        f"{py_parse_input()}\n"
        f"{call_line}\n"
        f"{print_line}\n\n"
        f'if __name__ == "__main__":\n'
        f"    main()\n"
    )


# ─── Write files ─────────────────────────────────────────────
def write_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    rel = os.path.relpath(file_path, base_dir)
    print(f"  \u2714  {rel}")


print(f"\n\U0001f527 Generating boilerplate for: {problem}\n")

write_file(os.path.join(boilerplate_dir, "function.cpp"), gen_cpp_boilerplate())
write_file(os.path.join(boilerplate_dir, "function.js"), gen_js_boilerplate())
write_file(os.path.join(boilerplate_dir, "function.py"), gen_py_boilerplate())
write_file(
    os.path.join(full_boilerplate_dir, "function.cpp"), gen_cpp_full_boilerplate()
)
write_file(os.path.join(full_boilerplate_dir, "function.js"), gen_js_full_boilerplate())
write_file(os.path.join(full_boilerplate_dir, "function.py"), gen_py_full_boilerplate())

print(f"\n\u2705 Done! 6 files generated.\n")
