---
title: Reverse Linked List
slug: reverse-linked-list
difficulty: easy
tags: [linked-list, recursion]
---

## Description

Given the `head` of a singly linked list, **reverse the list** and return the reversed list's head.

## Examples

### Example 1

**Input:**

```
1 2 3 4 5
```

**Output:**

```
5 4 3 2 1
```

### Example 2

**Input:**

```
1 2
```

**Output:**

```
2 1
```

### Example 3

**Input:**

```

```

**Output:**

```

```

**Explanation:** An empty list reversed is still empty.

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Hints

- **Hint 1 — Iterative:** Keep track of three pointers: `prev`, `curr`, and `next`. On each step, reverse the `curr->next` pointer to point to `prev`, then advance all three pointers forward.
- **Hint 2 — Recursive:** Assume the rest of the list beyond the current node is already reversed. The current node's `next->next` should point back to the current node. Then set `current->next = null` to avoid a cycle.

## Follow-Up

> Can you solve it both **iteratively** and **recursively**?
