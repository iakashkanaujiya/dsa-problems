---
title: Valid Parentheses
slug: valid-parentheses
difficulty: easy
tags: [string, stack]
---

## Description

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is **valid**.

A string is valid if:

1. Open brackets must be closed by the **same type** of brackets.
2. Open brackets must be closed in the **correct order**.
3. Every close bracket has a corresponding open bracket.

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

### Example 2

**Input:**

```
s = "()[]{}"
```

**Output:**

```
true
```

### Example 3

**Input:**

```
s = "(]"
```

**Output:**

```
false
```

### Example 4

**Input:**

```
s = "([)]"
```

**Output:**

```
false
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`

## Hints

- **Hint 1:** Use a stack. When you see an opening bracket, push it. When you see a closing bracket, check if the top of the stack matches.
- **Hint 2:** If the stack is empty at any point when you encounter a closing bracket, or the top doesn't match, the string is invalid. At the end, the stack must be empty.
