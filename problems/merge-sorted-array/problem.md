---
title: Merge Sorted Array
slug: merge-sorted-array
difficulty: easy
tags: [array, two-pointers, sorting]
---

## Description

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing** order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in **non-decreasing** order. The final sorted array should be stored inside `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements to be merged and the last `n` elements are set to `0` and should be ignored.

Return the merged array.

## Examples

### Example 1

**Input:**

```
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
```

**Output:**

```
1 2 2 3 5 6
```

### Example 2

**Input:**

```
nums1 = [1]
m = 1
nums2 = []
n = 0
```

**Output:**

```
1
```

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Hints

- **Hint 1:** Start merging from the **end** of both arrays. Place the larger element at position `m+n-1` of `nums1`.
- **Hint 2:** Use three pointers: `p1 = m-1`, `p2 = n-1`, `p = m+n-1`. Move backwards, always picking the larger of `nums1[p1]` and `nums2[p2]`.
