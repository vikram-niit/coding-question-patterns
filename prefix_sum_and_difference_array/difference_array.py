def apply_range_updates(arr, updates):
    n = len(arr)
    diff = [0] * (n + 1)

    for l, r, val in updates:
        diff[l] += val
        if r + 1 < n:
            diff[r + 1] -= val

    # Rebuild the final array
    for i in range(1, n):
        diff[i] += diff[i - 1]

    return diff[:-1]


arr = [0, 0, 0, 0, 0]
updates = [(1, 3, 2), (2, 4, 3)]
print(apply_range_updates(arr, updates))
# Output: [0, 2, 5, 5, 3]
