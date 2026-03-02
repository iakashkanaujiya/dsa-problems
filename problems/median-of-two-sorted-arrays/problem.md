---
title: Median of Two Sorted Arrays
slug: median-of-two-sorted-arrays
difficulty: hard
tags: [array, binary-search, divide-and-conquer]
---

## Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

The overall run time complexity should be **O(log (m+n))**.

## Examples

### Example 1

**Input:**

```
nums1 = [1, 3]
nums2 = [2]
```

**Output:**

```
2.0
```

**Explanation:** Merged array = `[1, 2, 3]`, median = 2.

### Example 2

**Input:**

```
nums1 = [1, 2]
nums2 = [3, 4]
```

**Output:**

```
2.5
```

**Explanation:** Merged array = `[1, 2, 3, 4]`, median = (2 + 3) / 2 = 2.5.

## Constraints

- `nums1.length == m`, `nums2.length == n`
- `0 <= m <= 1000`, `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Hints

- **Hint 1:** Binary search on the smaller array. Partition both arrays such that all elements on the left are ≤ all elements on the right.
- **Hint 2:** For a partition at index `i` in `nums1` and `j = (m+n+1)/2 - i` in `nums2`, the partition is valid when `nums1[i-1] <= nums2[j]` and `nums2[j-1] <= nums1[i]`.
