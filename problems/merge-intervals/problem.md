# Merge Intervals

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all **overlapping intervals**, and return an array of the **non-overlapping intervals** that cover all the intervals in the input.

---

## Examples

### Example 1

**Input:**

```
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

**Output:**

```
1 3
2 6
→ merged → 1 6
8 10
15 18
```

Final output:

```
1 6
8 10
15 18
```

---

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

---

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`
