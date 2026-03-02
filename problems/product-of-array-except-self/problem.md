---
title: Product of Array Except Self
slug: product-of-array-except-self
difficulty: medium
tags: [array, prefix-sum]
---

## Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` **except** `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in **O(n)** time and **without using the division operation**.

## Examples

### Example 1

**Input:**

```
nums = [1, 2, 3, 4]
```

**Output:**

```
24 12 8 6
```

### Example 2

**Input:**

```
nums = [-1, 1, 0, -3, 3]
```

**Output:**

```
0 0 9 0 0
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

## Hints

- **Hint 1:** Build a **prefix product** array and a **suffix product** array. `answer[i] = prefix[i-1] * suffix[i+1]`.
- **Hint 2:** You can do it in O(1) extra space (excluding output): first pass fills `answer` with prefix products, second pass multiplies in suffix products using a running variable.

## Follow-Up

> Can you solve it with **O(1)** extra space (output array doesn't count)?
