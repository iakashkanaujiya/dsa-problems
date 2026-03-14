# DSA Problems & Code Generator

This repository contains a collection of Data Structures and Algorithms (DSA) problems along with an automated code generation system that creates consistent driver and boilerplate code across multiple programming languages.

## Supported Languages

- C++ (`cpp`)
- Python (`py`)
- JavaScript (`js`)
- TypeScript (`ts`)
- Java (`java`)
- Go (`go`)
- Rust (`rs`)

## Architecture & Structure

Each problem is contained in its own directory under `problems/` (e.g., `problems/2sum`). A typical problem directory includes:

- `problem.md`: Description, examples, constraints, and hints.
- `structure.json`: JSON configuration specifying the function name, parameters (with types), and the return type.
- `inputs/` and `outputs/`: Test cases. The first line is the number of test cases. Subsequent lines contain space-separated inputs mapped parameter-by-parameter.
- `boilerplate/`: Generated function stubs for users to implement their solution.
- `drivercode/`: Generated driver code (Main programs) that read space-separated inputs, execute the function, and print the exact expected string formats to `stdout`.
- `solution.*`: Reference solutions used for testing.

### Supported Data Types

The generator seamlessly supports primitives and complex types, including:

- Primitives: `int`, `float`, `double`, `bool`, `string`
- 1D Arrays: `int[]`, `float[]`, `double[]`, `bool[]`, `string[]`
- 2D Arrays: `int[][]`, `float[][]`, `double[][]`, `bool[][]`, `string[][]`
- Custom Node Structures: `ListNode` (Linked List) and `TreeNode` (Binary Tree). The drivers automatically include the structural definitions and parsing logic if these types are detected.

## Using the Code Generators

The code generators are written in Python and are located in the `code-generator/` directory.

### 1. Generating Boilerplate & Driver Code

To generate boilerplate and driver code for all supported languages simultaneously:

```bash
python code-generator/generate_all.py <path-to-structure.json> <problem-directory>
```

Example:

```bash
python code-generator/generate_all.py problems/2sum/structure.json problems/2sum
```

### 2. Individual Language Generation

You can also generate code for a specific language by running its designated build script:

```bash
python code-generator/cpp.py problems/2sum/structure.json problems/2sum
```

### 3. I/O Parsing

Test cases are stored as space-separated tokens instead of strict JSON structures to minimize processing logic in compiled languages. To convert clean human-readable array/list structures (e.g., `[1, 2, 3]`) into the space-separated formats required by the drivercode, use `parser.py`:

```bash
python code-generator/parser.py <path-to-structure.json> <input.txt> <output_parsed.txt>
```

## Adding a New Problem

1. Create a new directory under `problems/`.
2. Add a `problem.md` detailing the problem.
3. Create `structure.json` defining `functionName`, `parameters`, and `returnType`.
4. Create the `inputs` and `outputs` utilizing `parser.py` if needed.
5. Run `generate_all.py` to seamlessly build out all language tracks!
