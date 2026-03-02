---
title: Find Minimum in Rotated Sorted Array
slug: find-minimum-in-rotated-sorted-array
difficulty: medium
tags: [array, binary-search]
---

## Description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. Given the sorted rotated array `nums` of **unique** elements, return the **minimum element** of this array.

You must write an algorithm that runs in **O(log n)** time.

## Examples

### Example 1

**Input:**

```
nums = [3, 4, 5, 1, 2]
```

**Output:**

```
1
```

**Explanation:** Original array was `[1,2,3,4,5]` rotated 3 times.

### Example 2

**Input:**

```
nums = [4, 5, 6, 7, 0, 1, 2]
```

**Output:**

```
0
```

### Example 3

**Input:**

```
nums = [11, 13, 15, 17]
```

**Output:**

```
11
```

**Explanation:** Array was not rotated.

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All integers of `nums` are **unique**.
- `nums` is sorted and rotated between 1 and `n` times.

## Hints

- **Hint 1:** Use binary search. The minimum element is at the inflection point where `nums[i] > nums[i+1]`.
- **Hint 2:** If `nums[mid] > nums[right]`, the minimum is in the right half. Otherwise it's in the left half (including mid).
