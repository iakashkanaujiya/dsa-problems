# Reverse Linked List

Given the `head` of a singly linked list, **reverse the list** and return the reversed list's head.

---

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

---

### Example 2

**Input:**

```
1 2
```

**Output:**

```
2 1
```

---

### Example 3

**Input:**

```

```

**Output:**

```

```

**Explanation:** An empty list reversed is still empty.

---

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Approaches

### Iterative

Use three pointers (`prev = null`, `curr = head`, `next`). At each step:

1. Save `next = curr->next`
2. Reverse: `curr->next = prev`
3. Advance: `prev = curr`, `curr = next`

Return `prev` when `curr` is null.

### Recursive

Base case: empty list or single node. Otherwise, recurse on `head->next`, then wire `head->next->next = head` and `head->next = null`.

---

## Follow-Up

> Can you solve it both **iteratively** and **recursively**?
