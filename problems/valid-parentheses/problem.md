# Valid Parentheses

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is **valid**.

A string is valid if:

1. Open brackets must be closed by the **same type** of brackets.
2. Open brackets must be closed in the **correct order**.
3. Every close bracket has a corresponding open bracket.

---

## Examples

### Example 1

**Input:**

```
s = "()"
```

**Output:**

```
true
```

---

### Example 2

**Input:**

```
s = "()[]{}"
```

**Output:**

```
true
```

---

### Example 3

**Input:**

```
s = "(]"
```

**Output:**

```
false
```

---

### Example 4

**Input:**

```
s = "([)]"
```

**Output:**

```
false
```

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`
