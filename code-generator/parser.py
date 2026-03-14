import sys
import json


def parse_value(type_str, val_str):
    val_str = val_str.strip()

    if type_str in ["int", "float", "double", "bool"]:
        return val_str

    if type_str == "string":
        if val_str.startswith('"') and val_str.endswith('"'):
            return val_str[1:-1]
        return val_str

    if type_str.endswith("[]") and not type_str.endswith("[][]"):
        if val_str == "[]":
            return ""
        arr = json.loads(val_str)
        return " ".join(str(x) for x in arr)

    if type_str.endswith("[][]"):
        if val_str in ["[]", "[[]]"]:
            return "0"
        arr = json.loads(val_str)
        out = [str(len(arr))]
        for row in arr:
            if not row:
                out.append("0")
            else:
                out.append(str(len(row)))
                out.extend(str(x) for x in row)
        return " ".join(out)

    if type_str in ["ListNode", "TreeNode"]:
        if val_str == "[]":
            return ""
        arr = json.loads(
            val_str.replace("null", "None").replace("None", '"null"')
        )  # Handle null in Json
        return " ".join(str(x) for x in arr)

    return val_str


def process_file(structure_file, input_txt, output_txt):
    with open(structure_file, "r") as f:
        data = json.load(f)

    with open(input_txt, "r") as f:
        lines = f.read().strip().splitlines()

    if not lines:
        return

    t = int(lines[0].strip())
    params = data["parameters"]
    out_lines = [str(t)]

    idx = 1
    for _ in range(t):
        for p in params:
            val = parse_value(p["type"], lines[idx])
            out_lines.append(val)
            idx += 1

    with open(output_txt, "w") as f:
        f.write("\n".join(out_lines) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python parser.py <structure.json> <input.txt> <output.txt>")
        sys.exit(1)
    process_file(sys.argv[1], sys.argv[2], sys.argv[3])
