---
title: Climbing Stairs
slug: climbing-stairs
difficulty: easy
tags: [dynamic-programming, math, memoization]
---

## Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb **1** or **2** steps. In how many **distinct ways** can you climb to the top?

## Examples

### Example 1

**Input:**

```
n = 2
```

**Output:**

```
2
```

**Explanation:** Two ways: `1+1` or `2`.

### Example 2

**Input:**

```
n = 3
```

**Output:**

```
3
```

**Explanation:** Three ways: `1+1+1`, `1+2`, or `2+1`.

## Constraints

- `1 <= n <= 45`

## Hints

- **Hint 1:** Let `f(n)` be the number of ways to reach step `n`. You can arrive from step `n-1` (one step) or step `n-2` (two steps). So `f(n) = f(n-1) + f(n-2)`.
- **Hint 2:** This is the Fibonacci sequence! Base cases: `f(1) = 1`, `f(2) = 2`.
