# Binary Search

This project implements the **Binary Search** algorithm to find a target element in a sorted array efficiently.

## ⚙️ Algorithm
1. Initialize two pointers: `left` and `right`.
2. Find the middle index: `mid = (left + right) // 2`.
3. Compare `arr[mid]` with the target:
   - If equal → target found.
   - If smaller → search right half.
   - If larger → search left half.
4. Repeat until the element is found or the range is empty.

## 💻 Example
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 🕒 Complexity

Time: O(log n)

Space: O(1)
