# Bit Manipulation Cheatsheet

## 1. Basic Bit Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| AND (`&`) | Isolate/test bits | `x & 1` → checks if `x` is odd |
| OR (`|`)  | Set bits | `x | (1 << k)` → set k-th bit to 1 |
| XOR (`^`) | Toggle bits / detect differences | `x ^ (1 << k)` → flip k-th bit |
| NOT (`~`) | Invert all bits | `~x` |
| LEFT SHIFT (`<<`) | Multiply by powers of 2 | `x << 1` → multiply by 2 |
| RIGHT SHIFT (`>>`) | Divide by powers of 2 | `x >> 1` → divide by 2 |

**Tips:**  
- `a ^ a == 0` → XOR cancels identical numbers  
- `x & -x` → isolates rightmost set bit  

---

## 2. Common Patterns

### Pattern 1: Check if a number is a power of 2
```python
def is_power_of_2(x):
    return x > 0 and (x & (x - 1)) == 0
```

### Pattern 2: Count number of set bits
```python
def count_set_bits(x):
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count
```

### Pattern 3: Find the single non-repeating element
```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

### Pattern 4: Swap two numbers without a temporary variable
```python
a ^= b
b ^= a
a ^= b
```

### Pattern 5: Generate subsets / power set
```python
def subsets(nums):
    n = len(nums)
    res = []
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        res.append(subset)
    return res
```

### Pattern 6: Rightmost set bit
```python
rightmost_set_bit = x & -x
```

### Pattern 7: Count bits for all numbers 0…n (DP)
```python
def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp
```

### Pattern 8: Subsets with constraints

 - Use bitmasks and count_set_bits() to filter subsets (e.g., even sum or size k).

### Pattern 9: XOR basis / Maximum XOR

- Build a linear basis to maximize XOR of a subset (competitive programming).

### Pattern 10: Swap, reverse, or rotate bits
```python
# Swap two bits i and j
if ((x >> i) & 1) != ((x >> j) & 1):
    x ^= (1 << i) | (1 << j)

# Rotate bits left by k (n-bit integer)
rotated = (x << k) | (x >> (n - k))

```
