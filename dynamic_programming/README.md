# 🎒 0/1 Knapsack Problem (Space Optimized)

📘 **Problem**

Given `n` items with specific weights and values, and a knapsack with capacity `W`, find the maximum value that can be obtained by selecting items without exceeding the capacity.  
Each item can be chosen **at most once**.

**Example**
```
Input:
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7

Output: 9
Explanation: Items with weight 3 and 4 give max value 9.
```

⚙️ **Approach**

Use **1D Dynamic Programming**:
- Create a DP array `dp[w]` representing the max value achievable with capacity `w`.
- Iterate through each item and **update the DP array in reverse** to avoid overwriting previous results.

**Transition Formula**
```
dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
```

**Code (Python)**
```python
def knapsack_1d(weights, values, W):
    n = len(values)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[W]

# Example
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
print(knapsack_1d(weights, values, capacity))  # Output: 9
```

⏱️ **Complexity**
- Time: `O(n * W)`  
- Space: `O(W)`

🧠 **Key Insight**
Iterate DP array in **reverse** to preserve the previous state for 0/1 choices.
