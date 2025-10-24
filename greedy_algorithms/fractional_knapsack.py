def fractional_knapsack(weights, values, W):
    # Pair value and weight, and sort by value/weight ratio
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


# Example Usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print(fractional_knapsack(weights, values, capacity))  # Output: 240.0
