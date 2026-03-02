---
title: Palindrome Number
slug: palindrome-number
difficulty: easy
tags: [math]
---

## Description

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a palindrome when it reads the same forward and backward. For example, `121` is a palindrome while `123` is not.

## Examples

### Example 1

**Input:**

```
x = 121
```

**Output:**

```
true
```

### Example 2

**Input:**

```
x = -121
```

**Output:**

```
false
```

**Explanation:** Reads as `-121` forward and `121-` backward.

### Example 3

**Input:**

```
x = 10
```

**Output:**

```
false
```

**Explanation:** Reads as `01` backward.

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Hints

- **Hint 1:** All negative numbers are not palindromes. Numbers ending in 0 (except 0 itself) are not palindromes.
- **Hint 2:** Reverse only the second half of the number and compare with the first half. This avoids overflow from reversing the full number.

## Follow-Up

> Can you solve this **without converting the integer to a string**?
