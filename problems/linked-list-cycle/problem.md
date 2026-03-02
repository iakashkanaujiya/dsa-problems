---
title: Linked List Cycle
slug: linked-list-cycle
difficulty: easy
tags: [linked-list, two-pointers, hash-map]
---

## Description

Given `head`, the head of a linked list, determine if the linked list has a **cycle** in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list, otherwise return `false`.

> **Note:** For testing, input is given as a linear list. In the classic problem a `pos` argument indicates where the tail connects back (-1 means no cycle). Here we test with both cyclic and acyclic representations.

## Examples

### Example 1

**Input:**

```
head = [3, 2, 0, -4]
```

**Output:**

```
false
```

**Explanation:** No cycle in the linear representation.

### Example 2

**Input:**

```
head = [1, 2]
```

**Output:**

```
false
```

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Hints

- **Hint 1 — Hash Set:** Store visited node references in a hash set. If you revisit a node, there's a cycle.
- **Hint 2 — Floyd's Cycle Detection:** Use two pointers: slow moves 1 step, fast moves 2 steps. If they meet, there's a cycle. If fast reaches null, no cycle.

## Follow-Up

> Can you solve it using **O(1)** memory?
