---
title: Two Sum
slug: 2sum
difficulty: easy
tags: [array, hash-map]
---

## Description

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may **not** use the same element twice. You can return the answer in **any order**.

## Examples

### Example 1

**Input:**

```
nums = [2, 7, 11, 15]
target = 9
```

**Output:**

```
0 1
```

**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`. Return `[0, 1]`.

### Example 2

**Input:**

```
nums = [3, 2, 4]
target = 6
```

**Output:**

```
1 2
```

**Explanation:** `nums[1] + nums[2] = 2 + 4 = 6`. Return `[1, 2]`.

### Example 3

**Input:**

```
nums = [3, 3]
target = 6
```

**Output:**

```
0 1
```

**Explanation:** `nums[0] + nums[1] = 3 + 3 = 6`. Return `[0, 1]`.

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Exactly one valid answer exists.**

## Hints

- **Hint 1:** A brute force approach checks every pair. What is its time complexity?
- **Hint 2:** Can you use a hash map to remember numbers you've seen so far, and check if the complement (`target - nums[i]`) has already appeared?
- **Hint 3:** Iterate once: for each element, compute the complement. If it's in the map, you have your answer. Otherwise, store the current element in the map.

## Follow-Up

> Can you come up with an algorithm that runs in **O(n)** time?
