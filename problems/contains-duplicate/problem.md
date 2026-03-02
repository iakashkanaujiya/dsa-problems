---
title: Contains Duplicate
slug: contains-duplicate
difficulty: easy
tags: [array, hash-map, sorting]
---

## Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Examples

### Example 1

**Input:**

```
nums = [1, 2, 3, 1]
```

**Output:**

```
true
```

### Example 2

**Input:**

```
nums = [1, 2, 3, 4]
```

**Output:**

```
false
```

### Example 3

**Input:**

```
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

**Output:**

```
true
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

- **Hint 1:** Use a hash set. Insert each element; if it's already in the set, return true.
- **Hint 2:** Alternatively, sort the array and check adjacent elements.
