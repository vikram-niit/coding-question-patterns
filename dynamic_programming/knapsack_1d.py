def knapsack_1d(weights, values, W):
    n = len(values)
    dp = [0] * (W + 1)

    for i in range(n):
        # iterate in reverse to avoid overwriting needed values
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[W]


# Example Usage
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print(knapsack_1d(weights, values, capacity))  # Output: 9
