\# Prefix Sum and Difference Array



This project demonstrates the \*\*Prefix Sum\*\* and \*\*Difference Array\*\* techniques for efficient range sum queries and range updates.



\## ⚙️ Prefix Sum

Used to find the sum of any subarray in O(1) time after preprocessing.



```python

def prefix\_sum(arr):

&nbsp;   prefix = \[arr\[0]]

&nbsp;   for i in range(1, len(arr)):

&nbsp;       prefix.append(prefix\[-1] + arr\[i])

&nbsp;   return prefix

```



Usage:



```

arr = \[1, 2, 3, 4, 5]

prefix = prefix\_sum(arr)

\# Sum from index 1 to 3 -> 2 + 3 + 4 = 9

print(prefix\[3] - prefix\[0])  # Output: 9



```



\## ⚙️ Difference Array



Used to apply range updates efficiently and rebuild the final array using prefix sums.



```python

def apply\_range\_updates(arr, updates):

&nbsp;   n = len(arr)

&nbsp;   diff = \[0] \* (n + 1)

&nbsp;   for l, r, val in updates:

&nbsp;       diff\[l] += val

&nbsp;       if r + 1 < n:

&nbsp;           diff\[r + 1] -= val

&nbsp;   for i in range(1, n):

&nbsp;       diff\[i] += diff\[i - 1]

&nbsp;   return diff\[:-1]

```



Usage: 



```

arr = \[0, 0, 0, 0, 0]

updates = \[(1, 3, 2), (2, 4, 3)]

print(apply\_range\_updates(arr, updates))

\# Output: \[0, 2, 5, 5, 3]

```





\## 🕒 Complexity



Prefix Sum Query: O(1)



Range Update: O(1) per query



Build Time: O(n)

