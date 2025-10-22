\# Max Sum Subarray of Size K



\## Problem

Given an array of integers and a number `k`, find the maximum sum of any contiguous subarray of size `k`.



\## Example

Input: arr = \[2, 1, 5, 1, 3, 2], k = 3

Output: 9

Explanation: Subarray \[5, 1, 3] has the maximum sum = 9





\## Approach

Uses the \*\*sliding window\*\* technique to maintain the sum of a subarray of size `k`, updating the maximum sum as the window moves through the array.



\## Time Complexity

\- \*\*O(n)\*\* — Efficient single-pass solution.



\## Code (Python)

```python

def max\_sum\_subarray(arr, k):

&nbsp;   window\_sum = sum(arr\[:k])

&nbsp;   max\_sum = window\_sum



&nbsp;   for i in range(k, len(arr)):

&nbsp;       window\_sum += arr\[i] - arr\[i - k]

&nbsp;       max\_sum = max(max\_sum, window\_sum)



&nbsp;   return max\_sum



