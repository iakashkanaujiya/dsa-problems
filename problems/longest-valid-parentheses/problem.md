---
title: Longest Valid Parentheses
slug: longest-valid-parentheses
difficulty: hard
tags: [string, dynamic-programming, stack]
---

## Description

Given a string containing just the characters `'('` and `')'`, return the length of the **longest valid (well-formed) parentheses substring**.

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

### Example 3

**Input:**

```
s = ""
```

**Output:**

```
0
```

## Constraints

- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('` or `')'`.

## Hints

- **Hint 1 — Stack:** Push the index of `'('` onto the stack. For `')'`, pop from the stack. If the stack is empty, push the current index as a new base. Otherwise, the valid length is `i - stack.top()`.
- **Hint 2 — Dynamic Programming:** `dp[i]` = length of longest valid substring ending at `i`. If `s[i] == ')'` and `s[i-1] == '('`, then `dp[i] = dp[i-2] + 2`. If both are `')'` and `s[i - dp[i-1] - 1] == '('`, then extend.
- **Hint 3 — Two-pass scan:** Left-to-right: count `(` and `)`. When counts match, update max. When `)` exceeds `(`, reset. Then right-to-left with opposite condition to catch unclosed left parens.
