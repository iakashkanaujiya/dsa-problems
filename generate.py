import os
import sys
import subprocess


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate.py <problem_dir>")
        sys.exit(1)

    prob_dir = sys.argv[1]
    structure = os.path.join(prob_dir, "structure.json")

    print(structure)

    langs = ["cpp.py", "go.py", "java.py", "js.py", "py.py", "rs.py", "ts.py"]
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for lang in langs:
        script = os.path.join(base_dir, os.path.join("code-generator", lang))
        print(f"Running {lang} for {prob_dir}...")
        subprocess.run([sys.executable, script, structure, prob_dir], check=True)

    print("Done generating all templates.")


if __name__ == "__main__":
    main()
