# Prefix Sum and Difference Array

This project demonstrates the **Prefix Sum** and **Difference Array** techniques for efficient range sum queries and range updates.

## ⚙️ Prefix Sum
Used to find the sum of any subarray in O(1) time after preprocessing.

```python
def prefix_sum(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    return prefix
```

Usage:

```
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
# Sum from index 1 to 3 -> 2 + 3 + 4 = 9
print(prefix[3] - prefix[0])  # Output: 9

```

## ⚙️ Difference Array

Used to apply range updates efficiently and rebuild the final array using prefix sums.

```python
def apply_range_updates(arr, updates):
    n = len(arr)
    diff = [0] * (n + 1)
    for l, r, val in updates:
        diff[l] += val
        if r + 1 < n:
            diff[r + 1] -= val
    for i in range(1, n):
        diff[i] += diff[i - 1]
    return diff[:-1]
```

Usage: 

```
arr = [0, 0, 0, 0, 0]
updates = [(1, 3, 2), (2, 4, 3)]
print(apply_range_updates(arr, updates))
# Output: [0, 2, 5, 5, 3]

```

## 🕒 Complexity

- Prefix Sum Query: O(1)

- Range Update: O(1) per query

- Build Time: O(n)



