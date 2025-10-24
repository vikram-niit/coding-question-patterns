# 🎒 Fractional Knapsack Problem

📘 **Problem**

Given `n` items with specific weights and values, and a knapsack with capacity `W`, find the **maximum value** you can carry.  
Unlike 0/1 Knapsack, **you can take fractions of items**.

**Example**
```
Input:
weights = [10, 20, 30]
values = [60, 100, 120]
W = 50

Output: 240.0
Explanation: Take all of item1 (10,60) + all of item2 (20,100) + 2/3 of item3 (30,120)
```

⚙️ **Approach**

Use a **greedy strategy**:
1. Compute value-to-weight ratio for all items.
2. Sort items in descending order of ratio.
3. Take as much as possible from the top items until knapsack is full.

**Transition / Formula**
```
if W >= weight[i]:
    total_value += value[i]
    W -= weight[i]
else:
    total_value += value[i] * (W / weight[i])
    break
```

**Code (Python)**
```python
def fractional_knapsack(weights, values, W):
    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if W >= weight:
            total_value += value
            W -= weight
        else:
            total_value += value * (W / weight)
            break
    return total_value

# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(fractional_knapsack(weights, values, capacity))  # 240.0
```

⏱️ **Complexity**
- Time: `O(n log n)` (for sorting)
- Space: `O(n)`  

🧠 **Key Insight**
Greedy choice works because taking **highest value-per-weight items first** maximizes the total value.
