---
title: Merge Intervals
slug: merge-intervals
difficulty: medium
tags: [array, sorting, greedy]
---

## Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all **overlapping intervals**, and return an array of the **non-overlapping intervals** that cover all the intervals in the input.

## Examples

### Example 1

**Input:**

```
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

**Output:**

```
1 6
8 10
15 18
```

**Explanation:** Intervals `[1,3]` and `[2,6]` overlap and are merged into `[1,6]`.

### Example 2

**Input:**

```
intervals = [[1,4],[4,5]]
```

**Output:**

```
1 5
```

**Explanation:** `[1,4]` and `[4,5]` are overlapping.

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Hints

- **Hint 1:** Sort intervals by start time. Then sweep through: if the current interval overlaps the last merged one (start ≤ prev end), extend the prev end to max of both ends.
