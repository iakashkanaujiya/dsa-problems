---
title: Longest Substring Without Repeating Characters
slug: longest-substring-without-repeating
difficulty: medium
tags: [hash-map, sliding-window, string]
---

## Description

Given a string `s`, find the length of the **longest substring** without repeating characters.

A **substring** is a contiguous sequence of characters within a string.

## Examples

### Example 1

**Input:**

```
s = "abcabcbb"
```

**Output:**

```
3
```

**Explanation:** The longest substring without repeating characters is `"abc"`, of length 3.

### Example 2

**Input:**

```
s = "bbbbb"
```

**Output:**

```
1
```

**Explanation:** The answer is `"b"`, of length 1.

### Example 3

**Input:**

```
s = "pwwkew"
```

**Output:**

```
3
```

**Explanation:** The answer is `"wke"`, of length 3.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Hints

- **Hint 1:** Use the **sliding window** technique. Maintain a window `[left, right]` of unique characters.
- **Hint 2:** Use a hash map storing the most recent index of each character. When a repeat is found, jump `left` past the previous occurrence.
