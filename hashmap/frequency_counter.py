def frequency_count(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Usage
arr = [1, 2, 2, 3, 3, 3, 4]
print(frequency_count(arr))
# Output: {1: 1, 2: 2, 3: 3, 4: 1}

"""
# Frequency Counting using Hashmap

This implementation counts the frequency of each element in an array efficiently using a hashmap (Python dictionary).

## Algorithm
- Iterate through the array.
- For each element, increase its count in the hashmap.
- Return the hashmap with frequency counts.

## Example
```python
arr = [1, 2, 2, 3, 3, 3, 4]
print(frequency_count(arr))
```
# Output: {1: 1, 2: 2, 3: 3, 4: 1}


Complexity

Time: O(n)

Space: O(n)
"""
