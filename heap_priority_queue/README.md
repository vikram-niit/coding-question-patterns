# Kth Largest Element in an Array

### 🧩 Problem Statement
Given an unsorted array `nums` and an integer `k`, find the **kth largest element** in the array.

**Example:**
```python
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

### 💡 Approach

Use a Min-Heap (priority queue) of size k.

Push each number into the heap.
If heap size exceeds k, pop the smallest element.
After processing all numbers, the root of the heap is the kth largest.
This approach ensures we only keep track of the k largest elements seen so far.

## Complexity Analysis
Operation	Time Complexity	Space Complexity
Building heap	O(n log k)	O(k)

## 🧠 Example Trace
nums = [3, 2, 1, 5, 6, 4], k = 2
Heap evolution:
[3] → [2,3] → [3,5] → [5,6] → [5,6,4] → [5,6]
Result = 5

## 🧰 Requirements

Python 3.x

## 🚀 Run
python kth_largest.py

Output: 5
