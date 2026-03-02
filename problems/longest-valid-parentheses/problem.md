# Longest Valid Parentheses

Given a string containing just the characters `'('` and `')'`, return the length of the **longest valid (well-formed) parentheses substring**.

---

## Examples

### Example 1

**Input:**

```
s = "(()"
```

**Output:**

```
2
```

**Explanation:** The longest valid substring is `"()"`, length 2.

---

### Example 2

**Input:**

```
s = ")()())"
```

**Output:**

```
4
```

**Explanation:** The longest valid substring is `"()()"`, length 4.

---

### Example 3

**Input:**

```
s = ""
```

**Output:**

```
0
```

---

## Constraints

- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('` or `')'`.
