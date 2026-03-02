---
title: Maximum Subarray
slug: maximum-subarray
difficulty: medium
tags: [array, dynamic-programming, divide-and-conquer]
---

## Description

Given an integer array `nums`, find the **subarray** with the largest sum, and return its sum.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Examples

### Example 1

**Input:**

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

**Output:**

```
6
```

**Explanation:** The subarray `[4, -1, 2, 1]` has the largest sum = 6.

### Example 2

**Input:**

```
nums = [1]
```

**Output:**

```
1
```

### Example 3

**Input:**

```
nums = [5, 4, -1, 7, 8]
```

**Output:**

```
23
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

- **Hint 1 — Kadane's Algorithm:** Track the current running sum. If it drops below zero, reset it to zero (start a new subarray). At each step, update the global maximum.
- **Hint 2:** `curr = max(nums[i], curr + nums[i])` — either extend the existing subarray or start fresh from `nums[i]`.

## Follow-Up

> Can you solve this via **divide and conquer** in O(n log n)?
