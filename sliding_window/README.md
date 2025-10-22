# Max Sum Subarray of Size K



## Problem

Given an array of integers and a number `k`, find the maximum sum of any contiguous subarray of size `k`.



## Example

Input: arr = [2, 1, 5, 1, 3, 2], k = 3

Output: 9

Explanation: Subarray [5, 1, 3] has the maximum sum = 9



## Approach

Uses the **sliding window** technique to maintain the sum of a subarray of size `k`, updating the maximum sum as the window moves through the array.



## Time Complexity

- **O(n)** — Efficient single-pass solution.


## Approach
Uses the **sliding window** technique to maintain the sum of a subarray of size `k`, updating the maximum sum as the window moves through the array.

## Time Complexity
- **O(n)** — Efficient single-pass solution.

## Code (Python)
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```




