\# Binary Search



This project implements the \*\*Binary Search\*\* algorithm to find a target element in a sorted array efficiently.



\## ⚙️ Algorithm

1\. Initialize two pointers: `left` and `right`.

2\. Find the middle index: `mid = (left + right) // 2`.

3\. Compare `arr\[mid]` with the target:

&nbsp;  - If equal → target found.

&nbsp;  - If smaller → search right half.

&nbsp;  - If larger → search left half.

4\. Repeat until the element is found or the range is empty.



\## 💻 Example

```python

def binary\_search(arr, target):

&nbsp;   left, right = 0, len(arr) - 1

&nbsp;   while left <= right:

&nbsp;       mid = (left + right) // 2

&nbsp;       if arr\[mid] == target:

&nbsp;           return mid

&nbsp;       elif arr\[mid] < target:

&nbsp;           left = mid + 1

&nbsp;       else:

&nbsp;           right = mid - 1

&nbsp;   return -1



\## 🕒 Complexity



Time: O(log n)



Space: O(1)

