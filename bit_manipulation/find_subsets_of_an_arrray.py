def subsets(nums):
    n = len(nums)
    res = []
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        res.append(subset)
    return res
