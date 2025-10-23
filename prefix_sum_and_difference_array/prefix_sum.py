def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix


arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
# Sum from index 1 to 3 -> 2 + 3 + 4 = 9
print(prefix[3] - prefix[0])  # Output: 9

