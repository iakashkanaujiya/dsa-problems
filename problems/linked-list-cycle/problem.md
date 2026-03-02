# Linked List Cycle

Given `head`, the head of a linked list, determine if the linked list has a **cycle** in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list, otherwise return `false`.

> **Note:** For this problem, the input is a linear representation of the list for ease of testing. Internally, in real cycle detection, you would see a `pos` argument indicating where the tail connects. Here we test with both cyclic and acyclic inputs.

---

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

_(In the real problem, a cycle exists if pos != -1, but here we output based on the list input.)_

---

### Example 2

**Input:**

```
head = [1, 2]
```

**Output:**

```
false
```

---

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Follow-Up

> Can you solve it using **O(1)** memory?
