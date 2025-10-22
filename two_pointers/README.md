\# 🧊 Container With Most Water



\[!\[LeetCode - Container With Most Water](https://img.shields.io/badge/LeetCode-Container\_With\_Most\_Water-FFA116?logo=leetcode\&logoColor=white)](https://leetcode.com/problems/container-with-most-water/)

\[!\[Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)



\## 🚀 Problem



Given an array `height` where each element represents the height of a vertical line at position `i`, find two lines that together with the x-axis form a container that holds the \*\*most water\*\*.



\### Example



```python

Input: height = \[1,8,6,2,5,4,8,3,7]

Output: 49

```



\### Approach



Use two pointers, one starting at the beginning and one at the end of the array.

At each step, calculate the area formed by the two lines.

Move the pointer pointing to the shorter line inward.

Keep track of the maximum area found.

This approach runs in O(n) time with O(1) space.

