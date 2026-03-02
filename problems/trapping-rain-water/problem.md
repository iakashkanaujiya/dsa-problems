---
title: Trapping Rain Water
slug: trapping-rain-water
difficulty: hard
tags: [array, two-pointers, dynamic-programming, stack]
---

## Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Examples

### Example 1

**Input:**

```
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
```

**Output:**

```
6
```

**Explanation:** 6 units of rain water are trapped (the classic histogram illustration).

### Example 2

**Input:**

```
height = [4, 2, 0, 3, 2, 5]
```

**Output:**

```
9
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Hints

- **Hint 1 — DP Approach:** For each position `i`, the water level is `min(maxLeft[i], maxRight[i]) - height[i]`. Precompute prefix max from left and suffix max from right.
- **Hint 2 — Two Pointers:** Maintain left and right pointers. If `height[left] < height[right]`, process `left` using `leftMax`; otherwise process `right` using `rightMax`. Move the shorter side inward.
- **Hint 3 — Monotonic Stack:** Use a stack of indices. When you find a bar taller than the stack top, you've found a valley — calculate the water that would fill it.
