---
title: Merge K Sorted Lists
slug: merge-k-sorted-lists
difficulty: hard
tags: [linked-list, heap, divide-and-conquer, merge-sort]
---

## Description

You are given an array of `k` linked-lists, each sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

> **Note for testing:** The boilerplate passes a single flattened list. In a real interview setting, you receive `k` separate linked lists.

## Examples

### Example 1

**Input:**

```
lists = [[1,4,5],[1,3,4],[2,6]]
```

**Output:**

```
1 1 2 3 4 4 5 6
```

### Example 2

**Input:**

```
lists = []
```

**Output:**

```

```

### Example 3

**Input:**

```
lists = [[]]
```

**Output:**

```

```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Hints

- **Hint 1 — Min-Heap:** Use a min-heap. Push the head of each list. Always pop the minimum, add it to the result, and push its next node.
- **Hint 2 — Divide and Conquer:** Pair up lists and merge pairs. Repeat until one list remains. This gives O(n log k) time.
