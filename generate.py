"""
================================================================
generate.py — Auto-generates boilerplate & full-boilerplate
               from a problem's structure.json

Supported languages: C++, C, Go, Rust, TypeScript, Java, JavaScript, Python

Usage:
  python generate.py 2sum
  python generate.py reverse-linked-list
  python generate.py all        ← regenerates every problem
================================================================
"""

import sys
import os
import json

# ─── CLI ────────────────────────────────────────────────────
if len(sys.argv) < 2:
    print("Usage:   python generate.py <ProblemName|all>")
    print("Example: python generate.py 2sum")
    sys.exit(1)

base_dir = os.path.dirname(os.path.abspath(__file__))
problems_root = os.path.join(base_dir, "problems")

target = sys.argv[1]

if target == "all":
    problems = [
        d
        for d in os.listdir(problems_root)
        if os.path.isdir(os.path.join(problems_root, d))
    ]
else:
    problems = [target]


# ─── Per-problem generator ───────────────────────────────────
def generate_problem(problem):
    problem_dir = os.path.join(problems_root, problem)
    structure_file = os.path.join(problem_dir, "structure.json")
    boilerplate_dir = os.path.join(problem_dir, "boilerplate")
    full_boilerplate_dir = os.path.join(problem_dir, "full-boilerplate")

    if not os.path.exists(structure_file):
        print(f"  ERROR: structure.json not found at {structure_file}")
        return

    with open(structure_file, "r", encoding="utf-8") as f:
        schema = json.load(f)

    function_name = schema["functionName"]
    parameters = schema["parameters"]
    return_type = schema["returnType"]
    input_format = schema["inputFormat"]
    output_format = schema["outputFormat"]

    # ─── Type Maps ─────────────────────────────────────────────
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
    C_TYPES = {
        "int": "int",
        "int[]": "int*",
        "int[][]": "int**",
        "long": "long long",
        "long[]": "long long*",
        "string": "char*",
        "string[]": "char**",
        "bool": "int",
        "double": "double",
        "float": "float",
        "void": "void",
        "ListNode": "struct ListNode*",
    }
    GO_TYPES = {
        "int": "int",
        "int[]": "[]int",
        "int[][]": "[][]int",
        "long": "int64",
        "long[]": "[]int64",
        "string": "string",
        "string[]": "[]string",
        "bool": "bool",
        "double": "float64",
        "float": "float32",
        "void": "",
        "ListNode": "*ListNode",
    }
    RUST_TYPES = {
        "int": "i32",
        "int[]": "Vec<i32>",
        "int[][]": "Vec<Vec<i32>>",
        "long": "i64",
        "long[]": "Vec<i64>",
        "string": "String",
        "string[]": "Vec<String>",
        "bool": "bool",
        "double": "f64",
        "float": "f32",
        "void": "()",
        "ListNode": "Option<Box<ListNode>>",
    }
    TS_TYPES = {
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
        "ListNode": "ListNode | null",
    }
    JAVA_TYPES = {
        "int": "int",
        "int[]": "int[]",
        "int[][]": "int[][]",
        "long": "long",
        "long[]": "long[]",
        "string": "String",
        "string[]": "String[]",
        "bool": "boolean",
        "double": "double",
        "float": "float",
        "void": "void",
        "ListNode": "ListNode",
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

    def cpp_type(t):
        return CPP_TYPES.get(t, t)

    def c_type(t):
        return C_TYPES.get(t, t)

    def go_type(t):
        return GO_TYPES.get(t, t)

    def rust_type(t):
        return RUST_TYPES.get(t, t)

    def ts_type(t):
        return TS_TYPES.get(t, t)

    def java_type(t):
        return JAVA_TYPES.get(t, t)

    def js_type(t):
        return JS_TYPES.get(t, t)

    def py_type(t):
        return PY_TYPES.get(t, t)

    def uses_list_node():
        types = [p["type"] for p in parameters] + [return_type]
        return "ListNode" in types

    # ─── ListNode Preambles ──────────────────────────────────────────
    CPP_LISTNODE_PREAMBLE = """\
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

ListNode* buildList(const vector<int>& vals) {
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int v : vals) { cur->next = new ListNode(v); cur = cur->next; }
    return dummy.next;
}

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

    C_LISTNODE_PREAMBLE = """\
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* buildList(int* vals, int n) {
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* cur = &dummy;
    for (int i = 0; i < n; i++) {
        cur->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        cur->next->val = vals[i];
        cur->next->next = NULL;
        cur = cur->next;
    }
    return dummy.next;
}

void printList(struct ListNode* head) {
    int first = 1;
    while (head) {
        if (!first) printf(" ");
        printf("%d", head->val);
        first = 0;
        head = head->next;
    }
    printf("\\n");
}

"""

    GO_LISTNODE_PREAMBLE = """\
type ListNode struct {
    Val  int
    Next *ListNode
}

func buildList(vals []int) *ListNode {
    dummy := &ListNode{}
    cur := dummy
    for _, v := range vals {
        cur.Next = &ListNode{Val: v}
        cur = cur.Next
    }
    return dummy.Next
}

func printList(head *ListNode) {
    first := true
    for head != nil {
        if !first {
            fmt.Print(" ")
        }
        fmt.Print(head.Val)
        first = false
        head = head.Next
    }
    fmt.Println()
}

"""

    RUST_LISTNODE_PREAMBLE = """\
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

"""

    TS_LISTNODE_PREAMBLE = """\
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val: number = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(arr: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let cur = dummy;
  for (const v of arr) { cur.next = new ListNode(v); cur = cur.next; }
  return dummy.next;
}

function printList(head: ListNode | null): void {
  const vals: number[] = [];
  while (head) { vals.push(head.val); head = head.next; }
  console.log(vals.join(' '));
}

"""

    JAVA_LISTNODE_PREAMBLE = """\
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
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
  console.log(vals.join(' '));
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
    print(' '.join(vals))

"""

    # ─── Input Parsers ─────────────────────────────────────────────

    def cpp_parse_input():
        lines = []
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ in ("int[]", "long[]"):
                vt = "long long" if typ == "long[]" else "int"
                lines.append(f"    string _line{i}; getline(cin, _line{i});")
                lines.append(f"    istringstream _iss{i}(_line{i});")
                lines.append(
                    f"    {cpp_type(typ)} {field}; {{ {vt} _v; while(_iss{i} >> _v) {field}.push_back(_v); }}"
                )
            elif typ == "int[][]":
                lines.append(f"    {cpp_type(typ)} {field};")
                lines.append(
                    f"    {{ string _row; while(getline(cin, _row) && !_row.empty()) {{"
                )
                lines.append(
                    f"        istringstream _rs(_row); vector<int> _r; int _v;"
                )
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
                lines.append(
                    f"    {cpp_type(typ)} {field}; cin >> {field}; cin.ignore();"
                )
        return "\n".join(lines)

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

    def c_parse_input():
        lines = []
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ == "int[]":
                lines.append(f"    int {field}[100000]; int {field}_n = 0;")
                lines.append(
                    f"    {{ char _buf{i}[1000000]; fgets(_buf{i}, sizeof(_buf{i}), stdin);"
                )
                lines.append(f'      char* _tok = strtok(_buf{i}, " \\n");')
                lines.append(
                    f'      while (_tok) {{ {field}[{field}_n++] = atoi(_tok); _tok = strtok(NULL, " \\n"); }} }}'
                )
            elif typ == "ListNode":
                lines.append(f"    int _vals{i}[100000]; int _n{i} = 0;")
                lines.append(
                    f"    {{ char _buf{i}[1000000]; fgets(_buf{i}, sizeof(_buf{i}), stdin);"
                )
                lines.append(f'      char* _tok = strtok(_buf{i}, " \\n");')
                lines.append(
                    f'      while (_tok) {{ _vals{i}[_n{i}++] = atoi(_tok); _tok = strtok(NULL, " \\n"); }} }}'
                )
                lines.append(
                    f"    struct ListNode* {field} = buildList(_vals{i}, _n{i});"
                )
            elif typ == "string":
                lines.append(f'    char {field}[100000]; scanf("%s", {field});')
                lines.append(
                    f"    int _c; while((_c = getchar()) != '\\n' && _c != EOF);"
                )
            elif typ == "bool":
                lines.append(f'    int {field}; scanf("%d", &{field});')
                lines.append(
                    f"    int _c; while((_c = getchar()) != '\\n' && _c != EOF);"
                )
            else:
                lines.append(f'    {c_type(typ)} {field}; scanf("%d", &{field});')
                lines.append(
                    f"    int _c; while((_c = getchar()) != '\\n' && _c != EOF);"
                )
        return "\n".join(lines)

    def c_print_output(ret_var):
        out = output_format[0]
        typ = out["type"]
        if typ == "int[]":
            return (
                f"    for (int i = 0; i < result_n; i++) {{\n"
                f'        if (i) printf(" ");\n'
                f'        printf("%d", {ret_var}[i]);\n'
                f"    }}\n"
                f'    printf("\\n");'
            )
        elif typ == "ListNode":
            return f"    printList({ret_var});"
        elif typ == "bool":
            return f'    printf("%s\\n", {ret_var} ? "true" : "false");'
        elif typ == "void":
            return ""
        else:
            return f'    printf("%d\\n", {ret_var});'

    def go_parse_input():
        lines = [
            "    scanner := bufio.NewScanner(os.Stdin)",
            "    scanner.Buffer(make([]byte, 1024*1024), 1024*1024)",
            "    scanner.Split(bufio.ScanLines)",
            "    readLine := func() string {",
            "        scanner.Scan()",
            "        return strings.TrimSpace(scanner.Text())",
            "    }",
        ]
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ == "int[]":
                lines.append(f"    _parts{i} := strings.Fields(readLine())")
                lines.append(f"    {field} := make([]int, len(_parts{i}))")
                lines.append(
                    f"    for _i, _s := range _parts{i} {{ {field}[_i], _ = strconv.Atoi(_s) }}"
                )
            elif typ == "int[][]":
                lines.append(f"    var {field} [][]int")
                lines.append(f"    for {{")
                lines.append(f"        _line := readLine()")
                lines.append(f'        if _line == "" {{ break }}')
                lines.append(f"        _ps := strings.Fields(_line)")
                lines.append(f"        _row := make([]int, len(_ps))")
                lines.append(
                    f"        for _i, _s := range _ps {{ _row[_i], _ = strconv.Atoi(_s) }}"
                )
                lines.append(f"        {field} = append({field}, _row)")
                lines.append(f"    }}")
            elif typ == "string[]":
                lines.append(f"    {field} := strings.Fields(readLine())")
            elif typ == "string":
                lines.append(f"    {field} := readLine()")
            elif typ == "bool":
                lines.append(f"    _bval{i} := readLine()")
                lines.append(f'    {field} := _bval{i} == "true" || _bval{i} == "1"')
            elif typ == "ListNode":
                lines.append(f"    _parts{i} := strings.Fields(readLine())")
                lines.append(f"    _vals{i} := make([]int, len(_parts{i}))")
                lines.append(
                    f"    for _i, _s := range _parts{i} {{ _vals{i}[_i], _ = strconv.Atoi(_s) }}"
                )
                lines.append(f"    {field} := buildList(_vals{i})")
            elif typ in ("int", "long"):
                lines.append(f"    {field}, _ := strconv.Atoi(readLine())")
            elif typ in ("double", "float"):
                lines.append(f"    {field}, _ := strconv.ParseFloat(readLine(), 64)")
            else:
                lines.append(f"    {field}, _ := strconv.Atoi(readLine())")
        return "\n".join(lines)

    def go_print_output(ret_var):
        out = output_format[0]
        typ = out["type"]
        delim = out.get("delimiter", " ")
        if typ in ("int[]", "long[]"):
            return (
                f"    _strs := make([]string, len({ret_var}))\n"
                f"    for _i, _v := range {ret_var} {{ _strs[_i] = strconv.Itoa(_v) }}\n"
                f'    fmt.Println(strings.Join(_strs, "{delim}"))'
            )
        elif typ == "int[][]":
            return (
                f"    for _, _row := range {ret_var} {{\n"
                f"        _strs := make([]string, len(_row))\n"
                f"        for _i, _v := range _row {{ _strs[_i] = strconv.Itoa(_v) }}\n"
                f'        fmt.Println(strings.Join(_strs, "{delim}"))\n'
                f"    }}"
            )
        elif typ == "ListNode":
            return f"    printList({ret_var})"
        elif typ == "bool":
            return f'    if {ret_var} {{ fmt.Println("true") }} else {{ fmt.Println("false") }}'
        elif typ == "void":
            return ""
        else:
            return f"    fmt.Println({ret_var})"

    def rust_parse_input():
        lines = [
            "    use std::io::{self, BufRead};",
            "    let stdin = io::stdin();",
            "    let mut lines_iter = stdin.lock().lines().map(|l| l.unwrap());",
            "    let mut read_line = || lines_iter.next().unwrap_or_default();",
        ]
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ == "int[]":
                lines.append(
                    f"    let {field}: Vec<i32> = read_line().split_whitespace()"
                )
                lines.append(f"        .map(|x| x.parse().unwrap()).collect();")
            elif typ == "int[][]":
                lines.append(f"    let mut {field}: Vec<Vec<i32>> = Vec::new();")
                lines.append(f"    loop {{")
                lines.append(f"        let _line = read_line();")
                lines.append(f"        if _line.trim().is_empty() {{ break; }}")
                lines.append(
                    f"        {field}.push(_line.split_whitespace().map(|x| x.parse().unwrap()).collect());"
                )
                lines.append(f"    }}")
            elif typ == "string[]":
                lines.append(
                    f"    let {field}: Vec<String> = read_line().split_whitespace()"
                )
                lines.append(f"        .map(|x| x.to_string()).collect();")
            elif typ == "string":
                lines.append(
                    f"    let {field}: String = read_line().trim().to_string();"
                )
            elif typ == "bool":
                lines.append(f"    let _raw{i} = read_line();")
                lines.append(
                    f'    let {field}: bool = _raw{i}.trim() == "true" || _raw{i}.trim() == "1";'
                )
            elif typ == "ListNode":
                lines.append(
                    f"    let _vals{i}: Vec<i32> = read_line().split_whitespace()"
                )
                lines.append(f"        .map(|x| x.parse().unwrap()).collect();")
                lines.append(f"    let {field} = build_list(&_vals{i});")
            elif typ in ("int", "long"):
                cast = "i64" if typ == "long" else "i32"
                lines.append(
                    f"    let {field}: {cast} = read_line().trim().parse().unwrap();"
                )
            elif typ in ("double", "float"):
                cast = "f32" if typ == "float" else "f64"
                lines.append(
                    f"    let {field}: {cast} = read_line().trim().parse().unwrap();"
                )
            else:
                lines.append(
                    f"    let {field}: i32 = read_line().trim().parse().unwrap();"
                )
        return "\n".join(lines)

    def rust_print_output(ret_var):
        out = output_format[0]
        typ = out["type"]
        delim = out.get("delimiter", " ")
        if typ in ("int[]", "long[]"):
            return (
                f"    let _strs: Vec<String> = {ret_var}.iter().map(|x| x.to_string()).collect();\n"
                f'    println!("{{}}", _strs.join("{delim}"));'
            )
        elif typ == "int[][]":
            return (
                f"    for _row in &{ret_var} {{\n"
                f"        let _strs: Vec<String> = _row.iter().map(|x| x.to_string()).collect();\n"
                f'        println!("{{}}", _strs.join("{delim}"));\n'
                f"    }}"
            )
        elif typ == "ListNode":
            return f"    print_list({ret_var});"
        elif typ == "bool":
            return (
                f'    println!("{{}}", if {ret_var} {{ "true" }} else {{ "false" }});'
            )
        elif typ == "void":
            return ""
        else:
            return f'    println!("{{}}", {ret_var});'

    def ts_parse_input():
        lines = []
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ in ("int[]", "long[]"):
                lines.append(
                    f"    const {field}: number[] = lines[idx++].split(' ').map(Number);"
                )
            elif typ == "int[][]":
                lines.append(f"    const _{field}_rows: number[][] = [];")
                lines.append(
                    f"    while(idx < lines.length && lines[idx].trim() !== '') {{"
                )
                lines.append(
                    f"      _{field}_rows.push(lines[idx++].split(' ').map(Number));"
                )
                lines.append(f"    }}")
                lines.append(f"    idx++; // skip empty line")
                lines.append(f"    const {field}: number[][] = _{field}_rows;")
            elif typ == "string[]":
                lines.append(f"    const {field}: string[] = lines[idx++].split(' ');")
            elif typ == "string":
                lines.append(f"    const {field}: string = lines[idx++];")
            elif typ == "bool":
                lines.append(
                    f"    const {field}: boolean = lines[idx].trim() === 'true' || lines[idx++].trim() === '1';"
                )
                lines.append(
                    f"    if(!lines[idx-1].trim().includes('true') && !lines[idx-1].trim().includes('1')) idx++; else if(lines[idx-1].trim() === 'true' || lines[idx-1].trim()==='1') {{}} else idx++;"
                )  # wait, simpler:
                # Actually, simpler to just replace above bool statement
            elif typ == "ListNode":
                lines.append(
                    f"    const {field}: ListNode | null = buildList(lines[idx++].split(' ').map(Number));"
                )
            else:
                cast = "Number" if typ in ("int", "long", "double", "float") else ""
                lines.append(
                    f"    const {field}: {ts_type(typ)} = {cast}(lines[idx++]);"
                )
        # Fix bool:
        res = "\n".join(lines)
        res = res.replace(
            "const {field}: boolean = lines[idx].trim() === 'true' || lines[idx++].trim() === '1';",
            "const _{field}Str = lines[idx++];\n    const {field}: boolean = _{field}Str.trim() === 'true' || _{field}Str.trim() === '1';",
        )
        return res

    def ts_print_output(ret_var):
        out = output_format[0]
        typ = out["type"]
        delim = out.get("delimiter", " ")
        if typ in ("int[]", "long[]", "string[]"):
            return f"  console.log({ret_var}.join('{delim}'));"
        elif typ == "int[][]":
            return f"  {ret_var}.forEach(row => console.log(row.join('{delim}')));"
        elif typ == "ListNode":
            return f"  printList({ret_var});"
        elif typ == "bool":
            return f"  console.log({ret_var} ? 'true' : 'false');"
        elif typ == "void":
            return ""
        else:
            return f"  console.log({ret_var});"

    def java_parse_input():
        lines = ["        Scanner sc = new Scanner(System.in);"]
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ == "int[]":
                lines.append(
                    f'        int[] {field} = Arrays.stream(sc.nextLine().trim().split("\\\\s+")).mapToInt(Integer::parseInt).toArray();'
                )
            elif typ == "int[][]":
                lines.append(f"        List<int[]> _{field}list = new ArrayList<>();")
                lines.append(f"        while (sc.hasNextLine()) {{")
                lines.append(f"            String _row = sc.nextLine().trim();")
                lines.append(f"            if (_row.isEmpty()) break;")
                lines.append(
                    f'            _{field}list.add(Arrays.stream(_row.split("\\\\s+")).mapToInt(Integer::parseInt).toArray());'
                )
                lines.append(f"        }}")
                lines.append(
                    f"        int[][] {field} = _{field}list.toArray(new int[0][]);"
                )
            elif typ == "string[]":
                lines.append(
                    f'        String[] {field} = sc.nextLine().trim().split("\\\\s+");'
                )
            elif typ == "string":
                lines.append(f"        String {field} = sc.nextLine().trim();")
            elif typ == "bool":
                lines.append(
                    f'        boolean {field} = sc.nextLine().trim().equals("true") || sc.nextLine().trim().equals("1");'
                )
            elif typ == "ListNode":
                lines.append(
                    f'        int[] _vals{i} = Arrays.stream(sc.nextLine().trim().split("\\\\s+")).mapToInt(Integer::parseInt).toArray();'
                )
                lines.append(f"        ListNode {field} = buildList(_vals{i});")
            elif typ == "long":
                lines.append(
                    f"        long {field} = Long.parseLong(sc.nextLine().trim());"
                )
            elif typ in ("double", "float"):
                lines.append(
                    f"        {java_type(typ)} {field} = {java_type(typ).capitalize()}.parse{java_type(typ).capitalize()}(sc.nextLine().trim());"
                )
            else:
                lines.append(
                    f"        int {field} = Integer.parseInt(sc.nextLine().trim());"
                )
        return "\n".join(lines)

    def java_print_output(ret_var):
        out = output_format[0]
        typ = out["type"]
        delim = out.get("delimiter", " ")
        if typ == "int[]":
            return (
                f"        StringBuilder sb = new StringBuilder();\n"
                f"        for (int i = 0; i < {ret_var}.length; i++) {{\n"
                f'            if (i > 0) sb.append("{delim}");\n'
                f"            sb.append({ret_var}[i]);\n"
                f"        }}\n"
                f"        System.out.println(sb);"
            )
        elif typ == "int[][]":
            return (
                f"        for (int[] _row : {ret_var}) {{\n"
                f"            StringBuilder sb = new StringBuilder();\n"
                f"            for (int i = 0; i < _row.length; i++) {{\n"
                f'                if (i > 0) sb.append("{delim}");\n'
                f"                sb.append(_row[i]);\n"
                f"            }}\n"
                f"            System.out.println(sb);\n"
                f"        }}"
            )
        elif typ == "ListNode":
            return f"        printList({ret_var});"
        elif typ == "bool":
            return f'        System.out.println({ret_var} ? "true" : "false");'
        elif typ == "void":
            return ""
        else:
            return f"        System.out.println({ret_var});"

    def js_parse_input():
        lines = []
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ in ("int[]", "long[]"):
                lines.append(
                    f"    const {field} = lines[idx++].split(' ').map(Number);"
                )
            elif typ == "int[][]":
                lines.append(f"    const _{field}_rows = [];")
                lines.append(
                    f"    while(idx < lines.length && lines[idx].trim() !== '') {{"
                )
                lines.append(
                    f"      _{field}_rows.push(lines[idx++].split(' ').map(Number));"
                )
                lines.append(f"    }}")
                lines.append(f"    idx++; // skip empty line")
                lines.append(f"    const {field} = _{field}_rows;")
            elif typ == "string[]":
                lines.append(f"    const {field} = lines[idx++].split(' ');")
            elif typ == "string":
                lines.append(f"    const {field} = lines[idx++];")
            elif typ == "bool":
                lines.append(f"    const _{field}Str = lines[idx++];")
                lines.append(
                    f"    const {field} = _{field}Str.trim() === 'true' || _{field}Str.trim() === '1';"
                )
            elif typ == "ListNode":
                lines.append(
                    f"    const {field} = buildList(lines[idx++].split(' ').map(Number));"
                )
            else:
                cast = "Number" if typ in ("int", "long", "double", "float") else ""
                lines.append(f"    const {field} = {cast}(lines[idx++]);")
        return "\n".join(lines)

    def js_print_output(ret_var):
        out = output_format[0]
        typ = out["type"]
        delim = out.get("delimiter", " ")
        if typ in ("int[]", "long[]", "string[]"):
            return f"  console.log({ret_var}.join('{delim}'));"
        elif typ == "int[][]":
            return f"  {ret_var}.forEach(row => console.log(row.join('{delim}')));"
        elif typ == "ListNode":
            return f"  printList({ret_var});"
        elif typ == "bool":
            return f"  console.log({ret_var} ? 'true' : 'false');"
        elif typ == "void":
            return ""
        else:
            return f"  console.log({ret_var});"

    def py_parse_input():
        lines = []
        for i, f in enumerate(input_format):
            field, typ = f["field"], f["type"]
            if typ in ("int[]", "long[]"):
                lines.append(f"        {field} = list(map(int, lines[idx].split()))")
                lines.append(f"        idx += 1")
            elif typ == "int[][]":
                lines.append(f"        _{field}_rows = []")
                lines.append(f"        while idx < len(lines) and lines[idx].strip():")
                lines.append(
                    f"            _{field}_rows.append(list(map(int, lines[idx].split())))"
                )
                lines.append(f"            idx += 1")
                lines.append(f"        idx += 1 # skip empty line")
                lines.append(f"        {field} = _{field}_rows")
            elif typ == "string[]":
                lines.append(f"        {field} = lines[idx].split()")
                lines.append(f"        idx += 1")
            elif typ == "string":
                lines.append(f"        {field} = lines[idx]")
                lines.append(f"        idx += 1")
            elif typ == "bool":
                lines.append(f'        {field} = lines[idx].strip() in ("true", "1")')
                lines.append(f"        idx += 1")
            elif typ in ("double", "float"):
                lines.append(f"        {field} = float(lines[idx])")
                lines.append(f"        idx += 1")
            elif typ == "ListNode":
                lines.append(
                    f"        {field} = build_list(list(map(int, lines[idx].split())))"
                )
                lines.append(f"        idx += 1")
            else:
                lines.append(f"        {field} = int(lines[idx])")
                lines.append(f"        idx += 1")
        return "\n".join(lines)

    def py_print_output(ret_var):
        out = output_format[0]
        typ = out["type"]
        delim = out.get("delimiter", " ")
        if typ in ("int[]", "long[]"):
            return f'    print("{delim}".join(map(str, {ret_var})))'
        elif typ == "string[]":
            return f'    print("{delim}".join({ret_var}))'
        elif typ == "int[][]":
            return f'    for row in {ret_var}:\n        print("{delim}".join(map(str, row)))'
        elif typ == "ListNode":
            return f"    print_list({ret_var})"
        elif typ == "bool":
            return f'    print("true" if {ret_var} else "false")'
        elif typ == "void":
            return ""
        else:
            return f"    print({ret_var})"

    # ─── Boilerplate Generators ─────────────────────────────────────

    def gen_cpp_boilerplate():
        def param_str(p):
            t = cpp_type(p["type"])
            is_ref = p["type"].endswith("[]") or p["type"] == "string"
            return f"{t}{'&' if is_ref else ''} {p['name']}"

        preamble = CPP_LISTNODE_PREAMBLE if uses_list_node() else ""
        params = ", ".join(param_str(p) for p in parameters)
        return (
            f"{preamble}"
            f"class Solution {{\npublic:\n"
            f"    {cpp_type(return_type)} {function_name}({params}) {{\n"
            f"        // Write your code here\n"
            f"    }}\n"
            f"}};\n"
        )

    def gen_c_boilerplate():
        def param_str(p):
            t = c_type(p["type"])
            needs_n = p["type"] == "int[]"
            return f"{t} {p['name']}" + (f", int {p['name']}_n" if needs_n else "")

        preamble = (
            C_LISTNODE_PREAMBLE
            if uses_list_node()
            else "#include <stdio.h>\n#include <stdlib.h>\n\n"
        )
        params = ", ".join(param_str(p) for p in parameters)
        ret = c_type(return_type)
        return (
            f"{preamble}"
            f"{ret} {function_name}({params}) {{\n"
            f"    /* Write your code here */\n"
            f"}}\n"
        )

    def gen_go_boilerplate():
        preamble = GO_LISTNODE_PREAMBLE if uses_list_node() else ""

        def param_str(p):
            return f"{p['name']} {go_type(p['type'])}"

        params = ", ".join(param_str(p) for p in parameters)
        ret = go_type(return_type)
        ret_decl = f" {ret}" if ret else ""
        return (
            f"package main\n\n"
            f"{preamble}"
            f"func {function_name}({params}){ret_decl} {{\n"
            f"    // Write your code here\n"
            f"}}\n"
        )

    def gen_rust_boilerplate():
        preamble = RUST_LISTNODE_PREAMBLE if uses_list_node() else ""

        def param_str(p):
            return f"{p['name']}: {rust_type(p['type'])}"

        params = ", ".join(param_str(p) for p in parameters)
        ret = rust_type(return_type)
        ret_decl = f" -> {ret}" if ret != "()" else ""
        return (
            f"{preamble}"
            f"struct Solution;\n\n"
            f"impl Solution {{\n"
            f"    pub fn {function_name}({params}){ret_decl} {{\n"
            f"        // Write your code here\n"
            f"    }}\n"
            f"}}\n"
        )

    def gen_ts_boilerplate():
        preamble = TS_LISTNODE_PREAMBLE if uses_list_node() else ""

        def param_str(p):
            return f"{p['name']}: {ts_type(p['type'])}"

        params = ", ".join(param_str(p) for p in parameters)
        ret = ts_type(return_type)
        return (
            f"{preamble}"
            f"class Solution {{\n"
            f"  {function_name}({params}): {ret} {{\n"
            f"    // Write your code here\n"
            f"  }}\n"
            f"}}\n"
        )

    def gen_java_boilerplate():
        preamble = JAVA_LISTNODE_PREAMBLE if uses_list_node() else ""

        def param_str(p):
            return f"{java_type(p['type'])} {p['name']}"

        params = ", ".join(param_str(p) for p in parameters)
        ret = java_type(return_type)
        return (
            f"import java.util.*;\n\n"
            f"{preamble}"
            f"class Solution {{\n"
            f"    public {ret} {function_name}({params}) {{\n"
            f"        // Write your code here\n"
            f"    }}\n"
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
            f"class Solution {{\n"
            f"  {function_name}({param_names}) {{\n"
            f"    // Write your code here\n"
            f"  }}\n"
            f"}}\n"
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
            f"class Solution:\n"
            f"    def {function_name}(self, {params}) -> {ret_py}:\n"
            f"        # Write your code here\n"
            f"        pass\n"
        )

    # ─── Full-Boilerplate Generators ────────────────────────────────

    def gen_cpp_full_boilerplate():
        def param_str(p):
            t = cpp_type(p["type"])
            is_ref = p["type"].endswith("[]") or p["type"] == "string"
            return f"{t}{'&' if is_ref else ''} {p['name']}"

        preamble = CPP_LISTNODE_PREAMBLE if uses_list_node() else ""
        params = ", ".join(param_str(p) for p in parameters)
        call_args = ", ".join(p["name"] for p in parameters)
        ret_line = (
            f"    {cpp_type(return_type)} result = sol.{function_name}({call_args});"
            if return_type != "void"
            else f"    sol.{function_name}({call_args});"
        )
        print_line = cpp_print_output("result")
        parse_input_indented = "\n".join(
            "    " + line if line else line for line in cpp_parse_input().split("\n")
        )
        ret_line_indented = "\n".join(
            "        " + line.strip() for line in ret_line.split("\n")
        )
        print_line_indented = "\n".join(
            "        " + line.strip() for line in print_line.split("\n")
        )
        return (
            f"#include <bits/stdc++.h>\n"
            f"using namespace std;\n\n"
            f"{preamble}"
            f"##USER_CODE##\n\n"
            f"int main() {{\n"
            f"    ios_base::sync_with_stdio(false);\n"
            f"    cin.tie(NULL);\n\n"
            f"    string line;\n"
            f"    if (!getline(cin, line)) return 0;\n"
            f"    istringstream iss(line);\n"
            f"    int t;\n"
            f"    if (!(iss >> t)) return 0;\n"
            f"    while (t--) {{\n"
            f"{parse_input_indented}\n"
            f"        Solution sol;\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n"
            f"    }}\n"
            f"    return 0;\n"
            f"}}\n"
        )

    def gen_c_full_boilerplate():
        def param_str(p):
            t = c_type(p["type"])
            needs_n = p["type"] == "int[]"
            return f"{t} {p['name']}" + (f", int {p['name']}_n" if needs_n else "")

        preamble = (
            C_LISTNODE_PREAMBLE
            if uses_list_node()
            else "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n"
        )
        params = ", ".join(param_str(p) for p in parameters)
        call_args = ", ".join(
            p["name"] + (f", {p['name']}_n" if p["type"] == "int[]" else "")
            for p in parameters
        )
        ret_line = (
            f"    {c_type(return_type)} result = {function_name}({call_args});"
            if return_type != "void"
            else f"    {function_name}({call_args});"
        )
        print_line = c_print_output("result")
        parse_input_indented = "\n".join(
            "    " + line if line else line for line in c_parse_input().split("\n")
        )
        ret_line_indented = "\n".join("    " + line for line in ret_line.split("\n"))
        print_line_indented = "\n".join(
            "    " + line if line else line
            for line in c_print_output("result").split("\n")
        )
        return (
            f"{preamble}"
            f"##USER_CODE##\n\n"
            f"int main() {{\n"
            f"    char t_buf[256];\n"
            f"    if (!fgets(t_buf, sizeof(t_buf), stdin)) return 0;\n"
            f"    int t = atoi(t_buf);\n"
            f"    while (t--) {{\n"
            f"{parse_input_indented}\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n"
            f"    }}\n"
            f"    return 0;\n"
            f"}}\n"
        )

    def gen_go_full_boilerplate():
        preamble = GO_LISTNODE_PREAMBLE if uses_list_node() else ""

        def param_str(p):
            return f"{p['name']} {go_type(p['type'])}"

        params = ", ".join(param_str(p) for p in parameters)
        call_args = ", ".join(p["name"] for p in parameters)
        ret = go_type(return_type)
        ret_decl = f" {ret}" if ret else ""
        ret_line = (
            f"    result := {function_name}({call_args})"
            if return_type != "void"
            else f"    {function_name}({call_args})"
        )
        print_line = go_print_output("result")
        parse_input_indented = "\n".join(
            "    " + line if line.strip() else line
            for line in go_parse_input().split("\n")[7:]
        )
        scanner_code = "\n".join(go_parse_input().split("\n")[:7])
        ret_line_indented = "\n".join("    " + line for line in ret_line.split("\n"))
        print_line_indented = "\n".join(
            "    " + line if line else line
            for line in go_print_output("result").split("\n")
        )
        return (
            f"package main\n\n"
            f"import (\n"
            f'    "bufio"\n'
            f'    "fmt"\n'
            f'    "os"\n'
            f'    "strconv"\n'
            f'    "strings"\n'
            f")\n\n"
            f"{preamble}"
            f"##USER_CODE##\n\n"
            f"func main() {{\n"
            f"{scanner_code}\n"
            f"    tStr := readLine()\n"
            f'    if tStr == "" {{ return }}\n'
            f"    t, _ := strconv.Atoi(tStr)\n"
            f"    for i := 0; i < t; i++ {{\n"
            f"{parse_input_indented}\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n"
            f"    }}\n"
            f"}}\n"
        )

    def gen_rust_full_boilerplate():
        preamble = RUST_LISTNODE_PREAMBLE if uses_list_node() else ""

        def param_str(p):
            return f"{p['name']}: {rust_type(p['type'])}"

        params = ", ".join(param_str(p) for p in parameters)
        call_args = ", ".join(p["name"] for p in parameters)
        ret = rust_type(return_type)
        ret_decl = f" -> {ret}" if ret != "()" else ""
        ret_line = (
            f"    let result = Solution::{function_name}({call_args});"
            if return_type != "()"
            else f"    Solution::{function_name}({call_args});"
        )
        print_line = rust_print_output("result")
        parse_input_indented = "\n".join(
            "    " + line if line.strip() else line
            for line in rust_parse_input().split("\n")[4:]
        )
        scanner_code = "\n".join(rust_parse_input().split("\n")[:4])
        ret_line_indented = "\n".join("    " + line for line in ret_line.split("\n"))
        print_line_indented = "\n".join(
            "    " + line if line else line
            for line in rust_print_output("result").split("\n")
        )
        return (
            f"{preamble}"
            f"##USER_CODE##\n\n"
            f"fn main() {{\n"
            f"{scanner_code}\n"
            f"    let t_str = read_line();\n"
            f"    if t_str.is_empty() {{ return; }}\n"
            f"    let t: i32 = t_str.trim().parse().unwrap();\n"
            f"    for _ in 0..t {{\n"
            f"{parse_input_indented}\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n"
            f"    }}\n"
            f"}}\n"
        )

    def gen_ts_full_boilerplate():
        preamble = TS_LISTNODE_PREAMBLE if uses_list_node() else ""
        param_names = ", ".join(p["name"] for p in parameters)
        ret = ts_type(return_type)
        call_line = (
            f"  const result = sol.{function_name}({param_names});"
            if return_type != "void"
            else f"  sol.{function_name}({param_names});"
        )
        print_line = ts_print_output("result")
        parse_input_indented = ts_parse_input()
        ret_line_indented = "\n".join("  " + line for line in call_line.split("\n"))
        print_line_indented = "\n".join("  " + line for line in print_line.split("\n"))
        return (
            f'const readline = require("readline");\n'
            f"const rl = readline.createInterface({{ input: process.stdin }});\n"
            f"const lines: string[] = [];\n"
            f'rl.on("line", (line: string) => lines.push(line.trim()));\n'
            f'rl.on("close", () => {{\n'
            f"{preamble}\n"
            f"  ##USER_CODE##\n\n"
            f"  if (lines.length === 0) return;\n"
            f"  const t: number = Number(lines[0]);\n"
            f"  let idx = 1;\n"
            f"  for (let _i = 0; _i < t; _i++) {{\n"
            f"{parse_input_indented}\n"
            f"    const sol = new Solution();\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n"
            f"  }}\n"
            f"}});\n"
        )

    def gen_java_full_boilerplate():
        preamble = JAVA_LISTNODE_PREAMBLE if uses_list_node() else ""
        java_listnode_helpers = ""
        if uses_list_node():
            java_listnode_helpers = (
                "\n    static ListNode buildList(int[] vals) {\n"
                "        ListNode dummy = new ListNode(0);\n"
                "        ListNode cur = dummy;\n"
                "        for (int v : vals) { cur.next = new ListNode(v); cur = cur.next; }\n"
                "        return dummy.next;\n"
                "    }\n\n"
                "    static void printList(ListNode head) {\n"
                "        StringBuilder sb = new StringBuilder();\n"
                "        boolean first = true;\n"
                "        while (head != null) {\n"
                "            if (!first) sb.append(' ');\n"
                "            sb.append(head.val);\n"
                "            first = false;\n"
                "            head = head.next;\n"
                "        }\n"
                "        System.out.println(sb);\n"
                "    }\n"
            )

        def param_str(p):
            return f"{java_type(p['type'])} {p['name']}"

        call_args = ", ".join(p["name"] for p in parameters)
        ret_line = (
            f"        {java_type(return_type)} result = new Solution().{function_name}({call_args});"
            if return_type != "void"
            else f"        new Solution().{function_name}({call_args});"
        )
        print_line = java_print_output("result")
        parse_input_indented = "\n".join(
            "    " + line if line.strip() else line
            for line in java_parse_input().split("\n")[1:]
        )
        scanner_code = "\n".join(java_parse_input().split("\n")[:1])
        ret_line_indented = "\n".join("    " + line for line in ret_line.split("\n"))
        print_line_indented = "\n".join(
            "    " + line if line else line
            for line in java_print_output("result").split("\n")
        )
        return (
            f"import java.util.*;\n\n"
            f"{preamble}"
            f"##USER_CODE##\n\n"
            f"public class Main {{\n"
            f"{java_listnode_helpers}"
            f"    public static void main(String[] args) {{\n"
            f"{scanner_code}\n"
            f"        if (!sc.hasNextLine()) return;\n"
            f"        int t = Integer.parseInt(sc.nextLine().trim());\n"
            f"        while (t-- > 0) {{\n"
            f"{parse_input_indented}\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n"
            f"        }}\n"
            f"    }}\n"
            f"}}\n"
        )

    def gen_js_full_boilerplate():
        preamble = JS_LISTNODE_PREAMBLE if uses_list_node() else ""
        param_names = ", ".join(p["name"] for p in parameters)
        call_line = (
            f"  const result = sol.{function_name}({param_names});"
            if return_type != "void"
            else f"  sol.{function_name}({param_names});"
        )
        print_line = js_print_output("result")
        parse_input_indented = js_parse_input()
        ret_line_indented = "\n".join("  " + line for line in call_line.split("\n"))
        print_line_indented = "\n".join("  " + line for line in print_line.split("\n"))
        return (
            f'const readline = require("readline");\n'
            f"const rl = readline.createInterface({{ input: process.stdin }});\n"
            f"const lines = [];\n"
            f'rl.on("line", (line) => lines.push(line.trim()));\n'
            f'rl.on("close", () => {{\n'
            f"{preamble}\n"
            f"  ##USER_CODE##\n\n"
            f"  if (lines.length === 0) return;\n"
            f"  const t = Number(lines[0]);\n"
            f"  let idx = 1;\n"
            f"  for (let _i = 0; _i < t; _i++) {{\n"
            f"{parse_input_indented}\n"
            f"    const sol = new Solution();\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n"
            f"  }}\n"
            f"}});\n"
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
            f"    result = Solution().{function_name}({param_names})"
            if return_type != "None"
            else f"    Solution().{function_name}({param_names})"
        )
        print_line = py_print_output("result")
        parse_input_indented = py_parse_input()
        ret_line_indented = "\n".join("    " + line for line in call_line.split("\n"))
        print_line_indented = "\n".join(
            "    " + line for line in print_line.split("\n")
        )
        return (
            f"import sys\n"
            f"{typing_import}\n"
            f"{preamble}"
            f"##USER_CODE##\n\n"
            f"def main():\n"
            f"    lines = sys.stdin.read().strip().splitlines()\n"
            f"    if not lines: return\n"
            f"    t = int(lines[0].strip())\n"
            f"    idx = 1\n"
            f"    for _ in range(t):\n"
            f"{parse_input_indented}\n"
            f"{ret_line_indented}\n"
            f"{print_line_indented}\n\n"
            f'if __name__ == "__main__":\n'
            f"    main()\n"
        )

    # ─── Write files ─────────────────────────────────────────────
    def write_file(file_path, content):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        rel = os.path.relpath(file_path, base_dir)
        print(f"  ✔  {rel}")

    print(f"\n🔧 Generating boilerplate for: {problem}\n")

    # Boilerplate (what users see and edit)
    write_file(os.path.join(boilerplate_dir, "function.cpp"), gen_cpp_boilerplate())
    write_file(os.path.join(boilerplate_dir, "function.c"), gen_c_boilerplate())
    write_file(os.path.join(boilerplate_dir, "function.go"), gen_go_boilerplate())
    write_file(os.path.join(boilerplate_dir, "function.rs"), gen_rust_boilerplate())
    write_file(os.path.join(boilerplate_dir, "function.ts"), gen_ts_boilerplate())
    write_file(os.path.join(boilerplate_dir, "function.java"), gen_java_boilerplate())
    write_file(os.path.join(boilerplate_dir, "function.js"), gen_js_boilerplate())
    write_file(os.path.join(boilerplate_dir, "function.py"), gen_py_boilerplate())

    # Full boilerplate (includes I/O harness for judge execution)
    write_file(
        os.path.join(full_boilerplate_dir, "function.cpp"), gen_cpp_full_boilerplate()
    )
    write_file(
        os.path.join(full_boilerplate_dir, "function.c"), gen_c_full_boilerplate()
    )
    write_file(
        os.path.join(full_boilerplate_dir, "function.go"), gen_go_full_boilerplate()
    )
    write_file(
        os.path.join(full_boilerplate_dir, "function.rs"), gen_rust_full_boilerplate()
    )
    write_file(
        os.path.join(full_boilerplate_dir, "function.ts"), gen_ts_full_boilerplate()
    )
    write_file(
        os.path.join(full_boilerplate_dir, "function.java"), gen_java_full_boilerplate()
    )
    write_file(
        os.path.join(full_boilerplate_dir, "function.js"), gen_js_full_boilerplate()
    )
    write_file(
        os.path.join(full_boilerplate_dir, "function.py"), gen_py_full_boilerplate()
    )

    print(f"\n✅ Done! 16 files generated for: {problem}\n")


# ─── Run ─────────────────────────────────────────────────────
for prob in problems:
    generate_problem(prob)
