# Three Sum

Given an integer array `nums`, return all the **unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set **must not contain duplicate triplets**.

---

## Examples

### Example 1

**Input:**

```
nums = [-1, 0, 1, 2, -1, -4]
```

**Output:**

```
-1 -1 2
-1 0 1
```

**Explanation:** The two distinct triplets that sum to zero are `[-1,-1,2]` and `[-1,0,1]`.

---

### Example 2

**Input:**

```
nums = [0, 1, 1]
```

**Output:**

```

```

**Explanation:** No triplet sums to zero.

---

### Example 3

**Input:**

```
nums = [0, 0, 0]
```

**Output:**

```
0 0 0
```

**Explanation:** The only triplet is `[0,0,0]`.

---

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

---

## Follow-Up

> Can you solve it in **O(n²)** time without using extra space for a hash set?
