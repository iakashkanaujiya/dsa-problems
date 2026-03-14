import json
import os
import sys


def get_cpp_type(type_str):
    mapping = {
        "int": "int",
        "float": "float",
        "double": "double",
        "bool": "bool",
        "string": "string",
        "int[]": "vector<int>",
        "float[]": "vector<float>",
        "double[]": "vector<double>",
        "bool[]": "vector<bool>",
        "string[]": "vector<string>",
        "int[][]": "vector<vector<int>>",
        "float[][]": "vector<vector<float>>",
        "double[][]": "vector<vector<double>>",
        "bool[][]": "vector<vector<bool>>",
        "string[][]": "vector<vector<string>>",
        "ListNode": "ListNode*",
        "TreeNode": "TreeNode*",
    }
    return mapping.get(type_str, type_str)


def get_cpp_read_logic(type_str, var_name):
    if (
        type_str == "int"
        or type_str == "float"
        or type_str == "double"
        or type_str == "bool"
    ):
        return f"""
        {get_cpp_type(type_str)} {var_name};
        if (!(iss >> {var_name})) {var_name} = 0;
"""
    elif type_str == "string":
        return f"""
        string {var_name};
        iss >> {var_name};
"""
    elif type_str.endswith("[]") and not type_str.endswith("[][]"):
        base_type = get_cpp_type(type_str[:-2])
        return f"""
        vector<{base_type}> {var_name};
        {base_type} _{var_name}_item;
        while (iss >> _{var_name}_item) {{
            {var_name}.push_back(_{var_name}_item);
        }}
"""
    elif type_str.endswith("[][]"):
        base_type = get_cpp_type(type_str[:-4])
        return f"""
        int _{var_name}_rows;
        iss >> _{var_name}_rows;
        vector<vector<{base_type}>> {var_name}(_{var_name}_rows);
        for(int i=0; i<_{var_name}_rows; i++) {{
            int _{var_name}_cols;
            iss >> _{var_name}_cols;
            {var_name}[i].resize(_{var_name}_cols);
            for(int j=0; j<_{var_name}_cols; j++) {{
                iss >> {var_name}[i][j];
            }}
        }}
"""
    elif type_str == "ListNode":
        return f"""
        ListNode* _{var_name}_dummy = new ListNode(0);
        ListNode* _{var_name}_curr = _{var_name}_dummy;
        int _{var_name}_val;
        while (iss >> _{var_name}_val) {{
            _{var_name}_curr->next = new ListNode(_{var_name}_val);
            _{var_name}_curr = _{var_name}_curr->next;
        }}
        ListNode* {var_name} = _{var_name}_dummy->next;
"""
    elif type_str == "TreeNode":
        return f"""
        vector<string> _{var_name}_tokens;
        string _{var_name}_token;
        while (iss >> _{var_name}_token) _{var_name}_tokens.push_back(_{var_name}_token);
        TreeNode* {var_name} = nullptr;
        if (!_{var_name}_tokens.empty() && _{var_name}_tokens[0] != "null") {{
            {var_name} = new TreeNode(stoi(_{var_name}_tokens[0]));
            queue<TreeNode*> q;
            q.push({var_name});
            int i = 1;
            while(!q.empty() && i < _{var_name}_tokens.size()) {{
                TreeNode* curr = q.front(); q.pop();
                if (_{var_name}_tokens[i] != "null") {{
                    curr->left = new TreeNode(stoi(_{var_name}_tokens[i]));
                    q.push(curr->left);
                }}
                i++;
                if (i < _{var_name}_tokens.size() && _{var_name}_tokens[i] != "null") {{
                    curr->right = new TreeNode(stoi(_{var_name}_tokens[i]));
                    q.push(curr->right);
                }}
                i++;
            }}
        }}
"""
    return ""


def get_cpp_write_logic(type_str, var_name):
    if (
        type_str == "int"
        or type_str == "float"
        or type_str == "double"
        or type_str == "bool"
        or type_str == "string"
    ):
        return f"""cout << {var_name} << "\\n";"""
    elif type_str.endswith("[]") and not type_str.endswith("[][]"):
        return f"""
        for (int i = 0; i < {var_name}.size(); i++) {{
            if (i > 0) cout << " ";
            cout << {var_name}[i];
        }}
        cout << "\\n";
"""
    elif type_str.endswith("[][]"):
        return f"""
        for (int i = 0; i < {var_name}.size(); i++) {{
            for (int j = 0; j < {var_name}[i].size(); j++) {{
                if (j > 0) cout << " ";
                cout << {var_name}[i][j];
            }}
            cout << "\\n";
        }}
"""
    elif type_str == "ListNode":
        return f"""
        ListNode* _{var_name}_curr = {var_name};
        bool _{var_name}_first = true;
        while (_{var_name}_curr) {{
            if (!_{var_name}_first) cout << " ";
            cout << _{var_name}_curr->val;
            _{var_name}_first = false;
            _{var_name}_curr = _{var_name}_curr->next;
        }}
        cout << "\\n";
"""
    elif type_str == "TreeNode":
        return f"""
        if (!{var_name}) {{
            cout << "\\n";
        }} else {{
            queue<TreeNode*> q;
            q.push({var_name});
            vector<string> res;
            while(!q.empty()) {{
                TreeNode* curr = q.front(); q.pop();
                if (curr) {{
                    res.push_back(to_string(curr->val));
                    q.push(curr->left);
                    q.push(curr->right);
                }} else {{
                    res.push_back("null");
                }}
            }}
            while(!res.empty() && res.back() == "null") res.pop_back();
            for(int i=0; i<res.size(); i++) {{
                if (i > 0) cout << " ";
                cout << res[i];
            }}
            cout << "\\n";
        }}
"""
    return ""


def generate_cpp(structure_file, problem_dir):
    with open(structure_file, "r") as f:
        data = json.load(f)

    # Need structs?
    needs_list = False
    needs_tree = False
    all_types = [p["type"] for p in data["parameters"]] + [data["returnType"]]
    for t in all_types:
        if "ListNode" in t:
            needs_list = True
        if "TreeNode" in t:
            needs_tree = True

    boilerplate_dir = os.path.join(problem_dir, "boilerplate")
    driver_dir = os.path.join(problem_dir, "drivercode")
    os.makedirs(boilerplate_dir, exist_ok=True)
    os.makedirs(driver_dir, exist_ok=True)

    # Boilerplate
    cpp_params = []
    for p in data["parameters"]:
        ctype = get_cpp_type(p["type"])
        if "vector" in ctype or "string" in ctype:
            cpp_params.append(f"{ctype}& {p['name']}")
        else:
            cpp_params.append(f"{ctype} {p['name']}")

    ret_type = get_cpp_type(data["returnType"])
    func_name = data["functionName"]

    boilerplate = ""
    if needs_list:
        boilerplate += "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr) {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int x, ListNode *next) : val(x), next(next) {}\n * };\n */\n"
    if needs_tree:
        boilerplate += "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n * };\n */\n"

    boilerplate += f"class Solution {{\npublic:\n    {ret_type} {func_name}({', '.join(cpp_params)}) {{\n        // Write your code here\n        \n    }}\n}};\n"

    with open(os.path.join(boilerplate_dir, "function.cpp"), "w") as f:
        f.write(boilerplate)

    # Drivercode
    driver = "#include <bits/stdc++.h>\nusing namespace std;\n\n"
    if needs_list:
        driver += "struct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\n"
    if needs_tree:
        driver += "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode() : val(0), left(nullptr), right(nullptr) {}\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}\n};\n\n"

    driver += "##USER_CODE##\n\n"
    driver += "int main()\n{\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n\n    string line;\n    if (!getline(cin, line)) return 0;\n    istringstream iss(line);\n    int t;\n    if (!(iss >> t)) return 0;\n    while (t--)\n    {\n"

    call_args = []
    for p in data["parameters"]:
        driver += "        getline(cin, line);\n"
        driver += "        iss.clear();\n"
        driver += "        iss.str(line);\n"
        driver += get_cpp_read_logic(p["type"], p["name"])
        call_args.append(p["name"])

    driver += "        Solution sol;\n"
    driver += f"        {ret_type} result = sol.{func_name}({', '.join(call_args)});\n"
    driver += get_cpp_write_logic(data["returnType"], "result")

    driver += "    }\n    return 0;\n}\n"

    with open(os.path.join(driver_dir, "function.cpp"), "w") as f:
        f.write(driver)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cpp.py <structure.json> <problem_dir>")
        sys.exit(1)
    generate_cpp(sys.argv[1], sys.argv[2])
