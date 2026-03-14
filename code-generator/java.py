import json
import os
import sys


def get_java_type(type_str):
    mapping = {
        "int": "int",
        "float": "float",
        "double": "double",
        "bool": "boolean",
        "string": "String",
        "int[]": "int[]",
        "float[]": "float[]",
        "double[]": "double[]",
        "bool[]": "boolean[]",
        "string[]": "String[]",
        "int[][]": "int[][]",
        "float[][]": "float[][]",
        "double[][]": "double[][]",
        "bool[][]": "boolean[][]",
        "string[][]": "String[][]",
        "ListNode": "ListNode",
        "TreeNode": "TreeNode",
    }
    return mapping.get(type_str, "Object")


def get_java_read_logic(type_str, var_name):
    if type_str == "int":
        return f"            int {var_name} = Integer.parseInt(sc.nextLine().trim());\n"
    elif type_str == "float":
        return (
            f"            float {var_name} = Float.parseFloat(sc.nextLine().trim());\n"
        )
    elif type_str == "double":
        return f"            double {var_name} = Double.parseDouble(sc.nextLine().trim());\n"
    elif type_str == "bool":
        return f"            boolean {var_name} = Boolean.parseBoolean(sc.nextLine().trim());\n"
    elif type_str == "string":
        return f"            String {var_name} = sc.nextLine().trim();\n"
    elif type_str == "int[]":
        return f'            String _{var_name}_line = sc.nextLine().trim();\n            int[] {var_name} = _{var_name}_line.isEmpty() ? new int[0] : Arrays.stream(_{var_name}_line.split("\\\\s+")).mapToInt(Integer::parseInt).toArray();\n'
    elif type_str == "float[]":
        return f"            String _{var_name}_line = sc.nextLine().trim();\n            float[] {var_name} = new float[0];\n"
    elif type_str == "string[]":
        return f'            String _{var_name}_line = sc.nextLine().trim();\n            String[] {var_name} = _{var_name}_line.isEmpty() ? new String[0] : _{var_name}_line.split("\\\\s+");\n'
    elif type_str.endswith("[][]"):
        if type_str == "int[][]":
            return f"            int[][] {var_name} = readInt2DArray(sc.nextLine().trim());\n"
        elif type_str == "string[][]":
            return f"            String[][] {var_name} = readString2DArray(sc.nextLine().trim());\n"
    elif type_str == "ListNode":
        return f"            ListNode {var_name} = buildList(sc.nextLine().trim());\n"
    elif type_str == "TreeNode":
        return f"            TreeNode {var_name} = buildTree(sc.nextLine().trim());\n"

    # Fallback to general read loop for non-streamable primitive arrays
    if type_str.endswith("[]") and not type_str.endswith("[][]"):
        base = type_str[:-2]
        parse = (
            f"{base.capitalize()}.parse{base.capitalize()}" if base != "string" else ""
        )
        return f"""            String _{var_name}_line = sc.nextLine().trim();
            String[] _{var_name}_parts = _{var_name}_line.isEmpty() ? new String[0] : _{var_name}_line.split("\\\\s+");
            {type_str} {var_name} = new {base}[_{var_name}_parts.length];
            for(int i=0; i<_{var_name}_parts.length; i++) {var_name}[i] = {parse}(_{var_name}_parts[i]);\n"""

    return f"            {type_str} {var_name} = sc.nextLine().trim();\n"


def get_java_write_logic(type_str, var_name):
    if type_str in ["int", "float", "double", "string", "bool"]:
        return f"            System.out.println({var_name});\n"
    elif type_str.endswith("[]") and not type_str.endswith("[][]"):
        return f"""            for(int i=0; i<{var_name}.length; i++) {{
                if(i > 0) System.out.print(" ");
                System.out.print({var_name}[i]);
            }}
            System.out.println();\n"""
    elif type_str.endswith("[][]"):
        return f"""            for(int i=0; i<{var_name}.length; i++) {{
                for(int j=0; j<{var_name}[i].length; j++) {{
                    if(j > 0) System.out.print(" ");
                    System.out.print({var_name}[i][j]);
                }}
                System.out.println();
            }}\n"""
    elif type_str == "ListNode":
        return f"            printList({var_name});\n"
    elif type_str == "TreeNode":
        return f"            printTree({var_name});\n"
    return f"            System.out.println({var_name});\n"


def generate_java(structure_file, problem_dir):
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
    java_params = ", ".join(
        [f"{get_java_type(p['type'])} {p['name']}" for p in data["parameters"]]
    )
    ret_type = get_java_type(data["returnType"])

    boilerplate = ""
    if needs_list:
        boilerplate += "/**\n * Definition for singly-linked list.\n * public class ListNode {\n *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n * }\n */\n"
    if needs_tree:
        boilerplate += "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left = left;\n *         this.right = right;\n *     }\n * }\n */\n"

    boilerplate += f"class Solution {{\n    public {ret_type} {func_name}({java_params}) {{\n        // Write your code here\n        \n    }}\n}}\n"

    with open(os.path.join(boilerplate_dir, "function.java"), "w") as f:
        f.write(boilerplate)

    # Drivercode
    driver = "import java.util.*;\nimport java.io.*;\n\n"

    if needs_list:
        driver += "class ListNode { int val; ListNode next; ListNode() {} ListNode(int val) { this.val = val; } ListNode(int val, ListNode next) { this.val = val; this.next = next; } }\n"
    if needs_tree:
        driver += "class TreeNode { int val; TreeNode left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; } TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; } }\n"

    driver += "##USER_CODE##\n\n"

    driver += "public class Main {\n"

    if needs_list:
        driver += '    static ListNode buildList(String line) { if (line.isEmpty()) return null; String[] tokens = line.split("\\\\s+"); ListNode dummy = new ListNode(0); ListNode curr = dummy; for (String t : tokens) { curr.next = new ListNode(Integer.parseInt(t)); curr = curr.next; } return dummy.next; }\n    static void printList(ListNode head) { boolean first = true; while (head != null) { if (!first) System.out.print(" "); System.out.print(head.val); first = false; head = head.next; } System.out.println(); }\n'
    if needs_tree:
        driver += '    static TreeNode buildTree(String line) { if (line.isEmpty() || line.startsWith("null")) return null; String[] tokens = line.split("\\\\s+"); TreeNode root = new TreeNode(Integer.parseInt(tokens[0])); Queue<TreeNode> q = new LinkedList<>(); q.add(root); int i = 1; while (!q.isEmpty() && i < tokens.length) { TreeNode curr = q.poll(); if (!tokens[i].equals("null")) { curr.left = new TreeNode(Integer.parseInt(tokens[i])); q.add(curr.left); } i++; if (i < tokens.length && !tokens[i].equals("null")) { curr.right = new TreeNode(Integer.parseInt(tokens[i])); q.add(curr.right); } i++; } return root; }\n    static void printTree(TreeNode root) { if (root == null) return; Queue<TreeNode> q = new LinkedList<>(); q.add(root); List<String> res = new ArrayList<>(); while (!q.isEmpty()) { TreeNode curr = q.poll(); if (curr != null) { res.add(String.valueOf(curr.val)); q.add(curr.left); q.add(curr.right); } else { res.add("null"); } } while (!res.isEmpty() && res.get(res.size()-1).equals("null")) res.remove(res.size()-1); System.out.println(String.join(" ", res)); }\n'

    if needs_2d:
        driver += '    static int[][] readInt2DArray(String line) { if (line.isEmpty()) return new int[0][0]; String[] tokens = line.split("\\\\s+"); if(tokens.length == 0 || tokens[0].equals("0")) return new int[0][0]; int rows = Integer.parseInt(tokens[0]); int[][] res = new int[rows][]; int idx = 1; for(int i=0; i<rows; i++) { int cols = Integer.parseInt(tokens[idx++]); res[i] = new int[cols]; for(int j=0; j<cols; j++) res[i][j] = Integer.parseInt(tokens[idx++]); } return res; }\n'
        driver += '    static String[][] readString2DArray(String line) { if (line.isEmpty()) return new String[0][0]; String[] tokens = line.split("\\\\s+"); if(tokens.length == 0 || tokens[0].equals("0")) return new String[0][0]; int rows = Integer.parseInt(tokens[0]); String[][] res = new String[rows][]; int idx = 1; for(int i=0; i<rows; i++) { int cols = Integer.parseInt(tokens[idx++]); res[i] = new String[cols]; for(int j=0; j<cols; j++) res[i][j] = tokens[idx++]; } return res; }\n'

    driver += "    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        int t = Integer.parseInt(sc.nextLine().trim());\n        while (t-- > 0) {\n"

    call_args = []
    for p in data["parameters"]:
        driver += get_java_read_logic(p["type"], p["name"])
        call_args.append(p["name"])

    driver += "            Solution sol = new Solution();\n"
    driver += (
        f"            {ret_type} result = sol.{func_name}({', '.join(call_args)});\n"
    )
    driver += get_java_write_logic(data["returnType"], "result")

    driver += "        }\n    }\n}\n"

    with open(os.path.join(driver_dir, "function.java"), "w") as f:
        f.write(driver)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: java python java.py <structure.json> <problem_dir>")
        sys.exit(1)
    generate_java(sys.argv[1], sys.argv[2])
